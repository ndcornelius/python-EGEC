import math
from random import randint

# Group operations for a group on Elliptic Curves for use in implementation of El-Gamal cryptosystem.

a = 0
b = 1
p = 5

def set_curve( c, d, e ):
  
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

        # One or both of the points is the infinity (identy) point
    if (x1, y1)  == ('e', 'e'):
        x3 = x2
        y3 = y2

    elif (x2, y2) == ('e', 'e'):
        x3 = x1
        y3 = y1

    elif x1 == x2 and y1 == y2: # The points are the same
        k = ((3*(x1**2) + a)*modinv(((2*y1 % p)), p)) % p
        x3 = ((k**2) - 2*x1) % p
        y3 = (k * (x1-x3) - y1) % p

    ################################################################

    elif x1 == x2: # The points are inverse to each other
        x3 = 'e'
        y3 = 'e'

    else:
        k = ((y2-y1)*modinv((x2-x1) % p, p)) % p

    #################################################################

        if x1 != x2: # The points are NOT inverse to each other
            x3 = ((k**2) - x1 - x2) % p
            y3 = (k * (x1-x3) - y1) % p

    #################################################################

        else:
            x3 = -1
            y3 = -1
    
    return (x3, y3)

    # An efficient algorithm for finding a certain power of the generator.
def ec_multiply(G, m):
    if m < 0: raise Exception( "Cannot multiply by a negative number")
    elif m == 0: return ('e', 'e')
    elif m == 1: return G 
    elif m % 2 == 0:
        z = ec_multiply(G, m/2)
        return ec_add(z, z)
    else:
        z = ec_add(ec_multiply(G, m-1), G)
        return ec_add(z, G)

 # egcd and modinv functions obtained from http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python. 
#Original source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

    # Recursive Euclidian Algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

    # Modular Inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

    # Simple VERY INEFFICIENT primality test
def isprime(x):
    if x == 1: return False

    elif x <= 0: return False

    elif x%2 == 0: return False

    else:
        for y in range(3, int(math.ceil(math.sqrt(x))), 2):
            if x % y == 0: return False
        return True

def gen_prime(lb, ub):

    while True:
        prime = randint(lb, ub)
        if isprime(prime) is True: return prime

    # Eulers criterion for determining if a number 'a' is a quadratic residue mod a pime 'p'.
def eulers_criterion(a, p):
    ec = pow(a, (p-1)//2, p)
    if ec == p-1: return -1
    else: return ec


    # Tonelli-Shanks algorithm
    # Assumes p is odd prime and a is a quadratic residue mod p
    # Returns 'a', one of two modular square roots. However, '-a' is also a solution.
def modular_sqrt(a, p):
    a = a % p    

    ec = eulers_criterion(a, p) # Checking to make sure that a is indeed a quadratic residue mod p
    if ec == -1: return 0
    
    s , e = p-1, 0
    while s % 2 == 0: # Factoring p-1 into s * 2^e where s is odd.
        s //= 2
        e += 1

    if e == 1: return pow(a, (p+1)//4, p)

    n = 2
    i = eulers_criterion(n, p) # Find an n that is a quadratic nonresidue
    while i != -1: 
        n += 1
        i = eulers_criterion(i, p)

    g = pow(n, s, p)
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    r = e

    while True:
        m = 1
        if b % p == 1: return x
        while pow(b, pow(2, m), p) != 1:
            m += 1

        d = pow (g, pow(2, r-m-1), p)
     
        g = (d * d) % p
        x = (x * d) % p
        b = (b * (d * d)) % p
        r = m

def num_points(a, b, p):
    num_points = 1
    a, b = a % p, b % p

    if (4 * (a**3) + 27 * (b**2)) % p == 0:
        s = "Curve does not form a group."
        raise Exception(s)

    for x in range(p):
        n = (pow(x, 3, p) + (a * x) + b) % p
        if modular_sqrt(n, p) != 0:
             num_points += 2

    return num_points
        
def find_generator(a, b, p):
    points = num_points(a, b, p)
    set_curve(a, b, p)

    for x in range(p):
        n = (pow(x, 3, p) + (a * x) + b) % p
        y = modular_sqrt(n, p)
 #       print("Mod root = %d" % (y))
        print( "(%d, %d)" % (x, y))

        if y != 0:
            order = 1
            u, v, = x, y
            while (u, v) != ('e', 'e'):
                c = ec_add((u,v), (x,y))
                order += 1
                u, v = c[0], c[1]
 #               print(order)
#                print(c)
         #       if order > points: break
            if order == points:
                return (x, y)

    return (-1, -1)
