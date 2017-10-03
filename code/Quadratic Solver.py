def quad_formula(a, b, c, discrim=None):
    """
    Implements quadratic formula ((-b +- sqrt(b**2 - 4ac)) / 2a)
    """
    if discrim is None:
        discrim = b**2 - 4*a*c

    if discrim < 0:
        return None
    else:
        sol1 = (-b + discrim**0.5) / 2*a
        sol2 = (-b - discrim**0.5) / 2*a

        return (sol1, sol2)


if __name__ == '__main__':
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Ente c: '))

    formula = quad_formula(a, b, c)

    if formula is None:
        print("There are no real solutions")
    else:
        print("The roots are x = {0} and x = {1}".format(*formula))
