# Group operations for a group on Elliptic Curves for use in implementation of El-Gamal cryptosystem.
from ModularMath import modular_inverse, modular_sqrt

a = 0
b = 1
p = 5


def set_curve(c, d, e):
  
    if (4*(c**3) + 27*(d**2)) % e == 0:
        print ("Invalid coefficients. Elliptic curve does not form a group.")
    else:
 
        global a
        global b
        global p
 
        a = c
        b = d
        p = e


def ec_add(m, n):

    x1, y1 = m
    x2, y2 = n

    # One or both of the points is the infinity (identity) point
    if (x1, y1)  == ('e', 'e'):
        x3 = x2
        y3 = y2

    elif (x2, y2) == ('e', 'e'):
        x3 = x1
        y3 = y1

    # The points are the same
    elif x1 == x2 and y1 == y2:
        k = ((3 * (x1 * x1) + a)*modular_inverse((2 * y1), p)) % p
        x3 = ((k * k) - (2 * x1)) % p
        y3 = (k * (x1 - x3) - y1) % p

    # The points are inverse to each other
    elif x1 == x2:
        x3 = 'e'
        y3 = 'e'

    # The points are distinct and NOT inverse to each other
    elif x1 != x2:
        k = ((y2 - y1) * modular_inverse((x2 - x1) % p, p)) % p
        x3 = ((k**2) - x1 - x2) % p
        y3 = (k * (x1 - x3) - y1) % p

    else:
        x3 = -1
        y3 = -1
    
    return x3, y3


def ec_multiply(G, m):  # An efficient algorithm for finding a certain power of the generator.
    if m < 0:
        s = "Cannot multiply by a negative number"
        raise Exception(s)

    elif m == 0:
        return 'e', 'e'

    elif m == 1:
        return G

    elif m % 2 == 0:
        z = ec_multiply(G, m/2)
        return ec_add(z, z)

    else:
        z = ec_add(ec_multiply(G, m-1), G)
        return ec_add(z, G)


def get_order(a, b, p):  # Finds the number of (x, y) solution pairs for the elliptic curve with the given coefficients
    num_points = 1
    a, b = a % p, b % p

    if (4 * (a**3) + 27 * (b**2)) % p == 0:
        s = "Curve does not form a group."
        raise Exception(s)

    for x in range(p):
        n = (pow(x, 3, p) + (a * x) + b) % p
        root = modular_sqrt(n, p)
        if root != -1:
            if root == 0:
                num_points += 1
            else:
                num_points += 2

    return num_points


def find_generator(a, b, p):
    num_points = get_order(a, b, p)
    set_curve(a, b, p)

    if num_points == 1:
        return 'e', 'e'

    for x in range(p):
        n = (pow(x, 3, p) + (a * x) + b) % p
        y = modular_sqrt(n, p)

        # print( "(%d, %d)" % (x, y))
        if y != -1 and y != 0:
            order = 1
            u, v, = x, y
            while (u, v) != ('e', 'e'):
                u, v = ec_add((u, v), (x, y))
                order += 1

            if order == num_points:
                return x, y

    return -1, -1
