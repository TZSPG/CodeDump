numbers = list(range(1,101))

# square sum
square_sum = sum([i**2 for i in numbers])

# Sum square
sum_square = sum(numbers) ** 2


print(sum_square - square_sum)
