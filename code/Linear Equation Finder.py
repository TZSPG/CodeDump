def gradient(x1, x2, y1, y2):
    deltax = abs(x2 - x1)
    deltay = abs(y2 - y1)
    return deltay / deltax

def equation(pointA, pointB):
    x1 = int(string_handler(pointA)[0])
    y1 = int(string_handler(pointA)[1])
    x2 = int(string_handler(pointB)[0])
    y2 = int(string_handler(pointB)[1])
    try:
        grad = gradient(x1, x2, y1, y2)
        intersect = y1 - grad * x1
        print('The equation of the line is y = {}x + {}'.format(grad, intersect))
    except ZeroDivisionError:
        print('The equation of the line is x = {}'.format(x1))

def string_handler(coordinate):
    # Coordinate is in string format (x, y), with or without spaces
    if coordinate[0] == '(' and coordinate[-1] == ')':
        coordinate = coordinate[1:-1]
    coordinate = coordinate.split(',')
    x = coordinate[0]
    y = coordinate[1].lstrip(' ')
    return x, y


point1 = input('Enter a coordinate in the format (x, y):  ')
point2 = input('Enter another coordinate in the format (x, y):  ')

equation(point1, point2)
