import json
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    return parser.parse_args()


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_biggest_bar(bar_list):
    return max(
        bar_list,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(bar_list):
    return min(
        bar_list,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )


def get_distance(longitude, latitude, bar):
    distance = ((longitude - bar['geometry']['coordinates'][0]) ** 2 -
                (latitude - bar['geometry']['coordinates'][1]) ** 2)
    return distance


def get_closest_bar(bar_list):
    return min(bar_list, key=lambda bar: get_distance(longitude, latitude, bar))


if __name__ == '__main__':
    args = create_parser()
    try:
        bar_list = load_data(args.file)['features']
        print('Самый большой бар: {}'.
            format(get_biggest_bar(bar_list)['properties']['Attributes']['Name']))
        print('Cамый маленький бар: {}'.
            format(get_smallest_bar(bar_list)['properties']['Attributes']['Name']))
        longitude = float(input('Введите долготу: '))
        latitude = float(input('Введите широту: '))
        print('Ближайший бар: {}'.
            format(get_closest_bar(bar_list)['properties']['Attributes']['Name']))
    except (FileNotFoundError, ValueError):
        print('Невозможно прочесть файл')
