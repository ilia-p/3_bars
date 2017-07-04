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

def get_bars_by_seat(bar_data):
    min_seats_quantity = 5
    bar_size_dict = defaultdict(list)
    for item in bar_data:
        if item['SeatsCount'] >= min_seats_quantity:
            bar_size_dict[item['SeatsCount']].append(item['Name'])
    return bar_size_dict

def get_smallest_bars(bar_size_dict):
    min_seat_bar_tuple = min(bar_size_dict.items())
    min_seat_bar = min_seat_bar_tuple[1]
    return min_seat_bar
    
def get_biggest_bars(bar_size_dict):
    max_seat_bar_tuple = max(bar_size_dict.items())
    max_seat_bar = max_seat_bar_tuple[1]
    return max_seat_bar

def get_min_max_bars_dict(min_seat_bar, max_seat_bar):
    bar_size_name = ['Бар(ы) с наименьшим количесвом мест', 'Бар(ы) с наибольшим количесвом мест']
    bar_size      = [min_seat_bar, max_seat_bar]
    bars          = dict(zip(bar_size_name, bar_size))
    return bars

def print_min_max_bars(bars):
    for item in bars:
        print('\n{}:'.format(item))
        print('\n'.join(bar for bar in bars[item]))   

def get_closest_bars(bar_data, longitude, latitude):
    bar_dist_dict = defaultdict(list)
    bar_coordinates_list=((item['geoData']['coordinates'],item['Name']) for item in bar_data)
    current_coord = (longitude, latitude)
    for bar in bar_coordinates_list:
        bar_coord = (bar[0][0], bar[0][1])
        distance  = round(great_circle(current_coord, bar_coord).km,1)
        bar_dist_dict[str(distance)].append(bar[1])
    bar_dist_tuple   = min(bar_dist_dict.items())
    bar_dist_nearest = bar_dist_tuple[1]
    return bar_dist_nearest
    
def print_closest_bars(bar_dist_nearest):
    print('\n{}:'.format('Ближайший(е) бар(ы)'))
    print('\n'.join(bar for bar in bar_dist_nearest)) 
    
if __name__ == '__main__':
    arg = parser.parse_args()
    bar_data = load_data(arg.path)
    bar_size_dict = get_bars_by_seat(bar_data)
    min_seat_bar = get_smallest_bars(bar_size_dict)
    max_seat_bar = get_biggest_bars(bar_size_dict)
    bars = get_min_max_bars_dict(min_seat_bar, max_seat_bar)
    print_min_max_bars(bars)
    longitude = float(input('\nВведите долготу: '))
    latitude  = float(input('Введите широту: '))
    bar_dist_nearest = get_closest_bars(bar_data, longitude, latitude)
    print_closest_bars(bar_dist_nearest)