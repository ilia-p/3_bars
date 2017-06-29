import json
import argparse
from collections import defaultdict, OrderedDict
# from geopy.distance import great_circle

parser = argparse.ArgumentParser(description = 'Path_to_file')
parser.add_argument('-p', '--path', type = str, required = True, help = 'Path to file with bar data in json')
arg = parser.parse_args()
filepath = arg.path

with open(filepath) as total_bar_list:
    bar_data = json.load(total_bar_list)

min_seats_quantity = 5
bar_size_dict = defaultdict(list)
for item in bar_data:
    if item['SeatsCount'] >= min_seats_quantity:
        bar_size_dict[item['SeatsCount']].append(item['Name'])
bar = OrderedDict(sorted(bar_size_dict.items()))

min_seat = list(bar.values())[0]
max_seat = list(bar.values())[-1]

print(min_seat, '\n')
print(max_seat)

# highest = max(bar_size_dict.values())
# print(highest)

# print([k for k, v in bar_size_dict.items() if v == highest])

# bar_size_dict = {item['SeatsCount'].append(item['Name']) for item in bar_data if item['SeatsCount'] >= min_seats_quantity}
# max_seat_bar = min(bar_seat_dict, key=lambda x: x[0] )

# example.sort( key=lambda x: x['key'] )

# print(max_bar_size_dict)

# 
# 
# seat_list_initial = list(bar_size_dict.keys())
# 
# seat_list = [seats for seats in seat_list_initial if seats >= min_seats_quantity]
# min_seat_bar = min(seat_list)

# print(min_seat_bar)

# min_seat_bar_list = []
# min_seat_bar_list.append(str(min_seat_bar))
# min_seat_bar_list += bar_size_dict[min_seat_bar]


# print(min_seat_bar_list)

