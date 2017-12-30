import json


file = 'bars.json'


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        return json.load(f)


data = load_data(file)
x = len(data['features'])


def get_name_and_seatscount():
    '''Function to create new dictionary with data: {'bar_name': number_of_seats}'''
    n_dict = []
    for i in range(x):
        name = data['features'][i]['properties']['Attributes']['Name']
        seatscount = data['features'][i]['properties']['Attributes']['SeatsCount']
        if seatscount != 0: #append to the list only the bars which have at least one seat
            n_dict.append([name, seatscount])
    return dict(n_dict)


new_data = get_name_and_seatscount()


def get_biggest_bar():
    '''Function to print the biggest bar by the number of seats'''
    max_seats = max(new_data.values())
    key = list(new_data.keys())[list(new_data.values()).index(max_seats)]
    print('Самый большой бар: ' + key)


def get_smallest_bar():
    '''Function to print the smallest bar according to the number of seats'''
    min_seats = min(new_data.values())
    key = list(new_data.keys())[list(new_data.values()).index(min_seats)]
    print('Самый маленький бар: ' + key)


def get_name_and_coords():
    '''Function to create new dictionary with data {'bar_name':coordinates}'''
    coords = []
    for i in range(x):
        name = data['features'][i]['properties']['Attributes']['Name']
        geometry = data['features'][i]['geometry']['coordinates']
        coords.append([name, geometry])
    return dict(coords)


def get_closest_bar(longitude, latitude):
    '''Function to print the closest bar'''
    coords = get_name_and_coords()
    dist = lambda key: ((longitude - coords[key][0]) ** 2 + (latitude - coords[key][1]) ** 2)
    found = min(coords, key=dist)
    print('Ближайший бар: ' + found)


if __name__ == '__main__':
    get_biggest_bar()
    get_smallest_bar()
    get_closest_bar(37.492603324522143, 55.827437174064421)
