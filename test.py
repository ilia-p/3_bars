import json
from collections import defaultdict
from math import sqrt

with open('data-2897-2016-11-23.json') as total_bar_list:
    bar_data = json.load(total_bar_list)

print(bar_data)

# bar_size_dict   = defaultdict(list)
# bar_coordinates_dict = defaultdict(list)

# for item in bar_data:
#     bar_size_dict[item['SeatsCount']].append(item['Name'])
# seat_list = list(bar_size_dict.keys())

# bar_coordinates_list = []

# for item in bar_data:
#     bar_coordinates_list.append((item['geoData']['coordinates'],item['Name']))

# print(bar_coordinates_list)

# coord = (37.58720622581934, 55.777682317891)
# nearest_dist = 0

# for bar in bar_coordinates_list:

#     coord_1 = bar[0][0]
#     coord_2 = bar[0][1]

#     # distance = sqrt((coord[0]-coord_1)**2 + (coord[1]-coord_2)**2)
#     distance = round(sqrt((coord[0]-coord_1)**2 + (coord[1]-coord_2)**2),15)
    
#     nearest_dist = 

#     print(distance)

# bar_coordinates_dict = {item['geoData']:item['Name'] for item in bar_data}
# coordinates_list = list(bar_coordinates_dict.keys())

# print(bar_coordinates_dict)

# print(max(seat_list))
# print(min(seat_list))
# max_seat_bar = max(seat_list)
# min_seat_bar = min(seat_list)
# print('Бар(ы) с максимальным количесвом мест - ', max_seat_bar)
# print('\n'.join(bar for bar in  bar_size_dict[max_seat_bar]))

# print('Бар(ы) с миниимальным количесвом мест - ', min_seat_bar)
# print('\n'.join(bar for bar in  bar_size_dict[min_seat_bar]))
# print(bar_size_dict)


# bar_size_dict = {item['SeatsCount']:[item['Name']] for item in bar_data}
# print(bar_size_dict)