# it works...

def is_palindrome(n):
    n_str = str(n)
    depth = 1
    while depth <= len(n_str)//2:
        if n_str[depth-1] != n_str[-depth]:
            return False
        else:
            depth += 1
    return True


a = 999
b = 999

while a > 100:
    while b > 100:
        if is_palindrome(a*b):
            print(a)
            print(b)
            print(a*b)
            break
        else:
            b -= 1

    a, b = a-1, a-1
