import json
import argparse

parser = argparse.ArgumentParser(description = 'Path_to_file')
parser.add_argument('-p', '--path', type = str, required = True, help = 'Path to file with json')

def load_data(filepath):
    with open(filepath) as data_file:
        data_list = [row for row in data_file]
    return data_list


# def get_biggest_bar(data):
#     pass


# def get_smallest_bar(data):
#     pass


# def get_closest_bar(data, longitude, latitude):
#     pass

def pretty_print_json(data_list):
    for data in data_list:
        json_data = json.loads(data)
        print(json.dumps(json_data, indent=4, sort_keys=True))

if __name__ == '__main__':
    arg = parser.parse_args()
    json_data = load_data(arg.path)
    pretty_print_json(json_data)