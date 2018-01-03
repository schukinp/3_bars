import json
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--longitude', type=float)
    parser.add_argument('--latitude', type=float)
    args = parser.parse_args()
    return args.file, args.longitude, args.latitude



def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_biggest_bar(bar_list):
    return max(
        bar_list,
        key=lambda bar:
        bar
        ['properties']
        ['Attributes']
        ['SeatsCount']
    )


def get_smallest_bar(bar_list):
    return min(
        bar_list,
        key=lambda bar:
        bar
        ['properties']
        ['Attributes']
        ['SeatsCount'])


def get_distance(longitude, latitude, bar):
    distance = ((longitude - bar['geometry']['coordinates'][0]) ** 2 -
                (latitude - bar['geometry']['coordinates'][1]) ** 2)
    return distance


def get_closest_bar(bar_list):
    return min(
        bar_list,
        key=lambda bar:
        get_distance(longitude, latitude, bar))


if __name__ == '__main__':
    filepath, longitude, latitude = get_arguments()
    bar_list = load_data(filepath)['features']
    print('Самый большой бар: {}'.
          format(get_biggest_bar(bar_list)
                           ['properties']
                           ['Attributes']
                           ['Name']))
    print('Cамый маленький бар: {}'.
          format(get_smallest_bar(bar_list)
                           ['properties']
                           ['Attributes']
                           ['Name']))
    print('Ближайший бар: {}'.
          format(get_closest_bar(bar_list)
                           ['properties']
                           ['Attributes']
                           ['Name']))
