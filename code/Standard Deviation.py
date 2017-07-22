# Source: https://www.mathsisfun.com/data/standard-deviation-formulas.html


def mean(data):
    return sum(data) / len(data)


def standard_deviation(data):
    ave = mean(data)
    return mean([(num - ave)**2 for num in data]) ** 0.5


if __name__ == '__main__':
    petals = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]
    print(standard_deviation(petals))
