import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        return json.load(file)


def get_bar_name_coordinates_and_seats():
    filtered_file = []
    for element in load_data(filepath)['features']:
        coords = element['geometry']['coordinates']
        bar_name = element['properties']['Attributes']['Name']
        seats = element['properties']['Attributes']['SeatsCount']
        if seats > 0:
            filtered_file.append([coords, bar_name, seats])
    return filtered_file


def get_biggest_bar():
    return tuple(max(get_bar_name_coordinates_and_seats(), key=lambda el: el[2])[1:3])


def get_smallest_bar():
    return tuple(min(get_bar_name_coordinates_and_seats(), key=lambda el: el[2])[1:3])


def get_closest_coords(longitude, latitude, element):
    distance = (longitude - element[0][0]) ** 2 + (latitude - element[0][1]) ** 2
    return distance


def get_closest_bar(longitude, latitude):
    return min(get_bar_name_coordinates_and_seats(), key=lambda el: get_closest_coords(longitude, latitude, el))[1]


filepath = input('Введите путь к файлу (например, c:/path/file.json): ')
longitude = float(input('Введите значение долготы: '))
latitude = float(input('Введите значение ширины: '))
print('Самый большой бар: %s с количеством мест: %d' % get_biggest_bar())
print('Cамый маленький бар: %s с количество мест: %d' % get_smallest_bar())
print('Ближайший бар: \'%s\'' % get_closest_bar(longitude, latitude))


if __name__ == '__main__':
    pass

