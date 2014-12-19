from random import randint
from math import ceil, sqrt

#  egcd and modular_inv functions obtained from
#  http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python and modified.
#  Original source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm


def egcd(a, b):  # Recursive Euclidian Algorithm
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modular_inverse(a, m):  # Modular Inverse
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse for %d mod %d does not exist' % (a, m))
    else:
        return x % m


def is_prime(x):  # Simple VERY INEFFICIENT primality test
    if x == 1:
        return False
    elif x <= 0:
        return False
    elif x % 2 == 0:
        return False

    else:
        for y in range(3, int(ceil(sqrt(x))) + 1, 2):
            if x % y == 0:
                return False
        return True


def gen_prime(lb, ub):  # Generates a prime between the lower bound and the upper bound

    while True:
        prime = randint(lb, ub)
        if is_prime(prime) is True:
            return prime


def eulers_criterion(a, p):  # Eulers criterion for determining if a number 'a' is a quadratic residue mod a pime 'p'.
    ec = pow(a, (p - 1) // 2, p)
    if ec == p-1: return -1
    else:
        return ec


    # Tonelli-Shanks algorithm
    # Assumes p is odd prime and a is a quadratic residue mod p
    # Returns 'a', one of two modular square roots. However, '-a' is also a solution.
def modular_sqrt(a, p):
    a = a % p

    if a == 0:
        return 0
    elif eulers_criterion(a, p) == -1:
        return -1

    s, e = p-1, 0
    while s % 2 == 0:  # Factoring p-1 into s * 2^e where s is odd.
        s //= 2
        e += 1
    if e == 1:
        return pow(a, ((p + 1) // 4), p)

    n = 1
    while eulers_criterion(n, p) != -1:  # Find an n that is a quadratic nonresidue
        n += 1

    g = pow(n, s, p)
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    r = e

    while True:
        k = b % p
        m = 0
        if k == 1:
            return x

        while k != 1:
            m += 1
            k = pow(k, 2, p)

        d = pow(g, pow(2, (r - 1 - m), p), p)

        g = (d * d) % p
        x = (x * d) % p
        b = (b * (d * d)) % p
        r = m