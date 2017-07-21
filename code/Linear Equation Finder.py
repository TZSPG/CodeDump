def equation(point_a, point_b):
    x1 = int(string_handler(point_a)[0])
    y1 = int(string_handler(point_a)[1])
    x2 = int(string_handler(point_b)[0])
    y2 = int(string_handler(point_b)[1])
    try:
        grad = gradient(x1, x2, y1, y2)
        intersect = y1 - grad * x1
        print('\n' + 'The equation of the line is y = {}x + {}'.format(grad, intersect))
    except ZeroDivisionError:
        print('\n' + 'The equation of the line is x = {}'.format(x1))


def gradient(x1, x2, y1, y2):
    deltax = abs(x2 - x1)
    deltay = abs(y2 - y1)
    return deltay / deltax


def string_handler(coordinate):
    """Coordinate is in string format (x, y), with or without spaces"""
    if coordinate[0] == '(' and coordinate[-1] == ')':
        coordinate = coordinate[1:-1]
    coordinate = coordinate.split(',')
    x = coordinate[0]
    y = coordinate[1].lstrip(' ')
    return x, y


if __name__ == '__main__':
    point1 = input('Enter a coordinate in the format (x, y):  ')
    point2 = input('Enter another coordinate in the format (x, y):  ')
    equation(point1, point2)
