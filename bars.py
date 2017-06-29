import json
import argparse
from collections import defaultdict, OrderedDict
from geopy.distance import great_circle

parser = argparse.ArgumentParser(description = 'Path_to_file')
parser.add_argument('-p', '--path', type = str, required = True, help = 'Path to file with bar data in json')

def load_data(filepath):
    with open(filepath) as total_bar_list:
        bar_data = json.load(total_bar_list)
    return bar_data

def order_bars_by_seat(bar_data):
    min_seats_quantity = 5
    bar_size_dict = defaultdict(list)
    for item in bar_data:
        if item['SeatsCount'] >= min_seats_quantity:
            bar_size_dict[item['SeatsCount']].append(item['Name'])
    oredered_bar_size_dict = OrderedDict(sorted(bar_size_dict.items()))
    return oredered_bar_size_dict

def get_smallest_bar(oredered_bar_size_dict):
    min_seat_bar_list = list(oredered_bar_size_dict.values())[0]
    return min_seat_bar_list
    
def print_smallest_bar(min_seat_bar_list):
    print('\nБар(ы) с наименьшим количесвом мест', '\n')
    print('\n'.join(bar for bar in min_seat_bar_list))

def get_biggest_bar(oredered_bar_size_dict):
    max_seat_bar_list = list(oredered_bar_size_dict.values())[-1]
    return max_seat_bar_list

def print_biggest_bar(max_seat_bar_list):
    print('\nБар(ы) с наибольшим количесвом мест', '\n')
    print('\n'.join(bar for bar in max_seat_bar_list))

def get_closest_bar(bar_data, search_radius, longitude, latitude):
    bar_dist_nearest_dict = defaultdict(list)
    bar_coordinates_list=((item['geoData']['coordinates'],item['Name']) for item in bar_data)
    current_coord = (longitude, latitude)
    for bar in bar_coordinates_list:
        bar_coord = (bar[0][0], bar[0][1])
        distance = round(great_circle(current_coord, bar_coord).km,1)
        if distance <= search_radius:
            bar_dist_nearest_dict[str(distance)].append(bar[1])
    return bar_dist_nearest_dict
    
def print_closest_bar(bar_dist_nearest_dict):
    if bar_dist_nearest_dict:
        for distance in sorted(bar_dist_nearest_dict.keys()):
            print('\n{} {}'.format(distance, 'км'))
            print('\n'.join(bar for bar in  bar_dist_nearest_dict[distance]))
    else:
        print('\nБаров в указанном радиусе поиска нет')

if __name__ == '__main__':
    arg = parser.parse_args()
    bar_data = load_data(arg.path)
    order_bars_by_seat = order_bars_by_seat(bar_data)
    min_seat_bar_list = get_smallest_bar(order_bars_by_seat)
    print_smallest_bar(min_seat_bar_list)
    max_seat_bar_list = get_biggest_bar(order_bars_by_seat)
    print_biggest_bar(max_seat_bar_list)
    search_radius = float(input('\nИщем ближайший бар\nВведите радиус поиска в км (например 1.5): '))
    longitude = float(input('Введите долготу: '))
    latitude  = float(input('Введите широту: '))
    bar_dist_nearest_dict = get_closest_bar(bar_data, search_radius, longitude, latitude)
    print_closest_bar(bar_dist_nearest_dict)