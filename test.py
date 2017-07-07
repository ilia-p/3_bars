import json
import argparse
from collections import defaultdict, OrderedDict
from geopy.distance import great_circle

parser = argparse.ArgumentParser(description = 'Path_to_file')
parser.add_argument('-p', '--path', type = str, required = True, help = 'Path to file with bar data in json')

def load_data(filepath):
    with open(filepath) as total_bar_list:
        bar_data = json.load(total_bar_list)
    # return bar_data
    max_seat = max(bar_data, key=lambda x:x['SeatsCount'])
    print(max_seat['Name'])

def get_bars_by_seat(bar_data):
    bar_size_dict = defaultdict(list)
    for item in bar_data:
        bar_size_dict[item['SeatsCount']].append(item['Name'])
    return bar_size_dict
    # bar = bar_size_dict
    # print(bar)

if __name__ == '__main__':
    arg = parser.parse_args()
    bar_data = load_data(arg.path)
    # bar_size_dict = get_bars_by_seat(bar_data)
    # get_bars_by_seat(bar_data)