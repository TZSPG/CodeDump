even_fibs = []

a = 1
b = 2

while a < 4000000:
    if a % 2 == 0:
        even_fibs.append(a)

    a, b = b, a + b

print(sum(even_fibs))