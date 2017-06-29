import json
import argparse
from collections import defaultdict
from geopy.distance import great_circle

parser = argparse.ArgumentParser(description = 'Path_to_file')
parser.add_argument('-p', '--path', type = str, required = True, help = 'Path to file with bar data in json')

def load_data(filepath):
    with open(filepath) as total_bar_list:
        bar_data = json.load(total_bar_list)
    return bar_data

def evaluate_smallest_bar(bar_data):
    bar_size_dict = defaultdict(list)
    for item in bar_data:
        bar_size_dict[item['SeatsCount']].append(item['Name'])
    seat_list_initial = list(bar_size_dict.keys())
    min_seats_quantity = 5
    seat_list = [seats for seats in seat_list_initial if seats >= min_seats_quantity]
    min_seat_bar = min(seat_list)
    min_seat_bar_list = []
    min_seat_bar_list.append(str(min_seat_bar))
    min_seat_bar_list += bar_size_dict[min_seat_bar]
    return min_seat_bar_list
    
def get_smallest_bar(min_seat_bar_list):
    min_seat = min_seat_bar_list[0]
    min_seat_list_bar = min_seat_bar_list[1:]
    print('\nБар(ы) с наименьшим количесвом мест - ', min_seat)
    print('\n'.join(bar for bar in min_seat_list_bar))

def evaluate_biggest_bar(bar_data):
    bar_size_dict = defaultdict(list)
    for item in bar_data:
        bar_size_dict[item['SeatsCount']].append(item['Name'])
    seat_list = list(bar_size_dict.keys())
    max_seat_bar = max(seat_list)
    max_seat_bar_list = []
    max_seat_bar_list.append(str(max_seat_bar))
    max_seat_bar_list += bar_size_dict[max_seat_bar]
    return max_seat_bar_list

def get_biggest_bar(min_seat_bar_list):
    max_seat = max_seat_bar_list[0]
    max_seat_list_bar = max_seat_bar_list[1:]
    print('\nБар(ы) с наибольшим количесвом мест - ', max_seat)
    print('\n'.join(bar for bar in max_seat_list_bar))


def evaluate_closest_bar(bar_data, search_radius, longitude, latitude):
    bar_dist_nearest_dict = defaultdict(list)
    bar_coordinates_list=((item['geoData']['coordinates'],item['Name']) for item in bar_data)
    current_coord = (longitude, latitude)
    for bar in bar_coordinates_list:
        bar_coord = (bar[0][0], bar[0][1])
        distance = round(great_circle(current_coord, bar_coord).km,1)
        if distance <= search_radius:
            bar_dist_nearest_dict[str(distance)].append(bar[1])
    return bar_dist_nearest_dict
    
def get_closest_bar(bar_dist_nearest_dict):
    if bar_dist_nearest_dict:
        for distance in sorted(bar_dist_nearest_dict.keys()):
            print('\n{} {}'.format(distance, 'км'))
            print('\n'.join(bar for bar in  bar_dist_nearest_dict[distance]))
    else:
        print('\nБаров в указанном радиусе поиска нет')

if __name__ == '__main__':
    arg = parser.parse_args()
    bar_data = load_data(arg.path)
    min_seat_bar_list = evaluate_smallest_bar(bar_data)
    get_smallest_bar(min_seat_bar_list)
    max_seat_bar_list = evaluate_biggest_bar(bar_data)
    get_biggest_bar(max_seat_bar_list)
    search_radius = float(input('\nИщем ближайший бар\nВведите радиус поиска в км (например 1.5): '))
    longitude = float(input('Введите долготу: '))
    latitude  = float(input('Введите широту: '))
    bar_dist_nearest_dict = evaluate_closest_bar(bar_data, search_radius, longitude, latitude)
    get_closest_bar(bar_dist_nearest_dict)