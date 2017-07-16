import json

with open('data-2897-2016-11-23.json') as total_bar_list:
        bar_data = json.load(total_bar_list)
print(bar_data[0]['Name'])
print(bar_data[0]['geoData']['coordinates'][0])
print(bar_data[0]['geoData']['coordinates'][1])