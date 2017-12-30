import json


file = 'bars.json'


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        return json.load(f)


data = load_data(file)
data_length = len(data['features'])


def get_bar_name_and_seatscount():
    new_dict = []
    for index in range(data_length):
        bar_name = data['features'][index]['properties']['Attributes']['Name']
        seatscount = data['features'][index]['properties']['Attributes']['SeatsCount']
        if seatscount != 0: #append to the list only the bars which have at least one seat
            new_dict.append([bar_name, seatscount])
    return dict(new_dict)


new_data = get_bar_name_and_seatscount()

def get_biggest_bar():
    max_seats = max(new_data.values())
    key = list(new_data.keys())[list(new_data.values()).index(max_seats)]
    print('Самый большой бар: ' + key)


def get_smallest_bar():
    min_seats = min(new_data.values())
    key = list(new_data.keys())[list(new_data.values()).index(min_seats)]
    print('Самый маленький бар: ' + key)


def get_bar_name_and_coordinates():
    coords = []
    for index in range(data_length):
        bar_name = data['features'][index]['properties']['Attributes']['Name']
        geometry = data['features'][index]['geometry']['coordinates']
        coords.append([bar_name, geometry])
    return dict(coords)


def get_closest_bar():
    longitude = float(input('Долгота: '))
    latitude = float(input('Широта: '))
    coords = get_bar_name_and_coordinates()
    distance = lambda key: ((longitude - coords[key][0]) ** 2 + (latitude - coords[key][1]) ** 2)
    found = min(coords, key=distance)
    print('Ближайший бар: ' + found)


if __name__ == '__main__':
    get_biggest_bar()
    get_smallest_bar()
    get_closest_bar()
