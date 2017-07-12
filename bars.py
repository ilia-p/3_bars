import json
import argparse
import os.path
import re
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

def get_closest_bars(bar_data, longitude, latitude):
    bar_dist_dict = {}
    current_coord = (longitude, latitude)
    bar_dist_dict = {item['Name']:round(sqrt((item['geoData']['coordinates'][0]-current_coord[0])**2 + 
                    (item['geoData']['coordinates'][1]-current_coord[1])**2),10) for item in bar_data}
    bar_min_dist_tuple = min(bar_dist_dict.items(), key=lambda x:x[1])
    bar_min_dist = bar_min_dist_tuple[0]
    return bar_min_dist
    
def print_target_bars(min_seat_bar, max_seat_bar, bar_min_dist):
    print('\n{}:\n{}'.format('Бар с наименьшим количесвом мест', min_seat_bar)) 
    print('\n{}:\n{}'.format('Бар с наибольшим количесвом мест', max_seat_bar)) 
    print('\n{}:\n{}'.format('Ближайший бар',bar_min_dist))
   

if __name__ == '__main__':
    
    arg = parser.parse_args()
    filepath = ''
    while True:
        if os.path.exists(arg.path):
            bar_data = load_data(arg.path)
            break
        elif os.path.exists(filepath):
            bar_data = load_data(filepath)
            break
        else:
            filepath = input('Такого пути/файла не существует, повторите ввод:\n')
            continue
    min_seat_bar = get_smallest_bars(bar_data)
    max_seat_bar = get_biggest_bars(bar_data)
    longitude = input('\nВведите долготу: ')
    while True:
        if re.compile(r'\d{2}\.\d*').search(longitude):
            longitude= float(longitude)
            break
        else:
            longitude = input('Введено некорректное значение, повторите ввод:\n')
            continue
    latitude  = input('Введите широту: ')
    while True:
        if re.compile(r'\d{2}\.\d*').search(latitude):
            latitude= float(latitude)
            break
        else:
            latitude = input('Введено некорректное значение, повторите ввод:\n')
            continue
    bar_min_dist = get_closest_bars(bar_data, longitude, latitude)
    print_target_bars(min_seat_bar, max_seat_bar, bar_min_dist)
        
