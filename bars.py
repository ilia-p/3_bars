import sys
import json
import argparse
import os.path
import re
from math import sqrt

parser = argparse.ArgumentParser(description = 'Path_to_file')
parser.add_argument('-p', '--path', type = str, required = True, help = 'Путь до файла с данными в формате json')

def check_path(arg):
    file_path = ''
    if os.path.exists(arg.path):
        filepath = arg.path
        return filepath
    sys.exit('Такого пути/файла не существует, повторите запуск')

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

def check_coordinate(coordinate):
    if re.compile(r'\d{2}\.\d*').search(coordinate):
        coordinate = float(coordinate)
        return coordinate
    sys.exit('Введено некорректное значение, повторите запуск')
        

def get_closest_bars(bar_data, longitude, latitude):
    current_coord = (longitude, latitude)
    bar_min_dist_data = min(bar_data, key=lambda x:round(sqrt((x['geoData']['coordinates'][0]-current_coord[0])**2 + 
                           (x['geoData']['coordinates'][1]-current_coord[1])**2),10))
    bar_min_dist = bar_min_dist_data['Name']
    return bar_min_dist
    
def print_target_bars(min_seat_bar, max_seat_bar, bar_min_dist):
    print('\n{}:\n{}'.format('Бар с наименьшим количесвом мест', min_seat_bar)) 
    print('\n{}:\n{}'.format('Бар с наибольшим количесвом мест', max_seat_bar)) 
    print('\n{}:\n{}'.format('Ближайший бар',bar_min_dist))
   
if __name__ == '__main__':
    arg = parser.parse_args()
    filepath = check_path(arg)
    bar_data = load_data(filepath)
    min_seat_bar = get_smallest_bars(bar_data)
    max_seat_bar = get_biggest_bars(bar_data)
    longitude_initial = input('\nВведите долготу: ')
    longitude = check_coordinate(longitude_initial)
    latitude_initial  = input('Введите широту: ')
    latitude = check_coordinate(latitude_initial)
    bar_min_dist = get_closest_bars(bar_data, longitude, latitude)
    print_target_bars(min_seat_bar, max_seat_bar, bar_min_dist)