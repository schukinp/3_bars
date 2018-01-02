import json
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--longitude', type=float)
    parser.add_argument('--latitude', type=float)
    args = parser.parse_args()
    return args


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_biggest_bar(bar_list):
    return max(bar_list,
               key=lambda bar:
               bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bar_list):
    return min(bar_list,
               key=lambda bar:
               bar['properties']['Attributes']['SeatsCount'])


def distance(longitude, latitude, bar_list):
    distance = (longitude - bar_list['geometry']['coordinates'][0]) ** 2 - \
               (latitude - bar_list['geometry']['coordinates'][1]) ** 2
    return distance


def get_closest_bar(bar_list):
    return min(bar_list,
               key=lambda bar:
               distance(longitude, latitude, bar))


if __name__ == '__main__':
    filepath = parser().file
    bar_list = load_data(filepath)['features']
    longitude = parser().longitude
    latitude = parser().latitude
    print('Самый большой бар: {}'.
          format(get_biggest_bar(bar_list)['properties']['Attributes']['Name']))
    print('Cамый маленький бар: {}'.
          format(get_smallest_bar(bar_list)['properties']['Attributes']['Name']))
    print('Ближайший бар: {}'.
          format(get_closest_bar(bar_list)['properties']['Attributes']['Name']))
