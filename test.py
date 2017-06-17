import json
from collections import defaultdict
from geopy.distance import vincenty, great_circle
# from math import sqrt


with open('data-2897-2016-11-23.json') as total_bar_list:
    bar_data = json.load(total_bar_list)

# print(bar_data)

bar_size_dict         = defaultdict(list)
bar_dist_nearest_dict = defaultdict(list)

for item in bar_data:
    bar_size_dict[item['SeatsCount']].append(item['Name'])
seat_list_initial = list(bar_size_dict.keys())
min_seats_quantity = 5
seat_list = [seats for seats in seat_list_initial if seats >= min_seats_quantity]


bar_coordinates_list=((item['geoData']['coordinates'],item['Name']) for item in bar_data)

search_radius = 1.5
current_coord = (37.58720622581934, 55.777682317891)

for bar in bar_coordinates_list:

    bar_coord = (bar[0][0], bar[0][1])
    distance = round(great_circle(current_coord, bar_coord).km,1)
    if distance <= search_radius:
    	bar_dist_nearest_dict[str(distance) + ' км'].append(bar[1])
# print(bar_dist_nearest_dict)

print('\nБлижайший(е) бар(ы) в радиусе ', search_radius, ' км')
for distance in sorted(bar_dist_nearest_dict.keys()):
	print('\n{}'.format(distance))
	print('\n'.join(bar for bar in  bar_dist_nearest_dict[distance]))



# print(max(seat_list))
# print(min(seat_list))
max_seat_bar = max(seat_list)
min_seat_bar = min(seat_list)
print('\nБар(ы) с максимальным количесвом мест - ', max_seat_bar)
print('\n'.join(bar for bar in  bar_size_dict[max_seat_bar]))

print('\nБар(ы) с миниимальным количесвом мест - ', min_seat_bar)
print('\n'.join(bar for bar in  bar_size_dict[min_seat_bar]))
# print(bar_size_dict)


# bar_size_dict = {item['SeatsCount']:[item['Name']] for item in bar_data}
# print(bar_size_dict)

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -71.395391)
# print(round(great_circle(newport_ri, cleveland_oh).m))