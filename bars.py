import json
import argparse
from math import sqrt

parser = argparse.ArgumentParser(description = 'Path_to_file')
parser.add_argument('-p', '--path', type = str, required = True, help = 'Path to file with bar data in json')

def load_data(filepath):
    with open(filepath) as total_bar_list:
        bar_data = json.load(total_bar_list)
    return bar_data

def get_smallest_bars(bar_data):
    min_seat_bar_dict = min(bar_data, key=lambda x:x['SeatsCount'])
    min_seat_bar = min_seat_bar_dict['Name']
    return min_seat_bar

def get_biggest_bars(bar_data):
    max_seat_bar_dict = max(bar_data, key=lambda x:x['SeatsCount'])
    max_seat_bar = max_seat_bar_dict['Name']
    return max_seat_bar

def get_min_max_bars_dict(min_seat_bar, max_seat_bar):
    bar_size_name = ['Бар с наименьшим количесвом мест', 'Бар с наибольшим количесвом мест']
    bar_size      = [min_seat_bar, max_seat_bar]
    bars          = dict(zip(bar_size_name, bar_size))
    return bars

def print_min_max_bars(bars):
    for item in bars:
        print('\n{}:\n{}'.format(item, bars[item])) 
   
def get_closest_bars(bar_data, longitude, latitude):
    bar_dist_dict = {}
    bar_coordinates_list=((item['geoData']['coordinates'],item['Name']) for item in bar_data)
    current_coord = (longitude, latitude)
    for bar in bar_coordinates_list:
        bar_coord = (bar[0][0], bar[0][1])
        distance  = round(sqrt((bar_coord[0]-current_coord[0])**2 + (bar_coord[1]-current_coord[1])**2),10)
        bar_dist_dict[bar[1]] = distance
    bar_min_dist_tuple = min(bar_dist_dict.items(), key=lambda x:x[1])
    bar_min_dist = bar_min_dist_tuple[0]
    return bar_min_dist
    
def print_closest_bars(bar_min_dist):
    print('\n{}:\n{}'.format('Ближайший бар',bar_min_dist))
   
if __name__ == '__main__':
    arg = parser.parse_args()
    bar_data = load_data(arg.path)
    min_seat_bar = get_smallest_bars(bar_data)
    max_seat_bar = get_biggest_bars(bar_data)
    bars = get_min_max_bars_dict(min_seat_bar, max_seat_bar)
    print_min_max_bars(bars)
    longitude = float(input('\nВведите долготу: '))
    latitude  = float(input('Введите широту: '))
    bar_min_dist = get_closest_bars(bar_data, longitude, latitude)
    print_closest_bars(bar_min_dist)