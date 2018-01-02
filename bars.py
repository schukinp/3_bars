import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-file')
args = parser.parse_args()
filepath = args.file


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


bar_list = load_data(filepath)['features']


def get_biggest_bar():
    return max(bar_list, key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar():
    return min(bar_list, key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_closest_bar(longitude, latitude):
    return min(bar_list, key=lambda bar: (longitude - bar['geometry']['coordinates'][0]) ** 2 -
                                         (latitude - bar['geometry']['coordinates'][1]) ** 2)


if __name__ == '__main__':
    longitude = float(input('Введите значение долготы: '))
    latitude = float(input('Введите значение ширины: '))
    print('Самый большой бар: {}'.format(get_biggest_bar()['properties']['Attributes']['Name']))
    print('Cамый маленький бар: {}'.format(get_smallest_bar()['properties']['Attributes']['Name']))
    print('Ближайший бар: {}'.format(get_closest_bar(longitude, latitude)['properties']['Attributes']['Name']))