
# Group operations for a group on Elliptic Curves for use in implementation of El-Gamal cryptosystem.

a = 0
b = 1
p = 5

def set_curve( c, d, e ):
  
    if (4*pow(c, 3) + 27*pow(d, 2)) % e == 0:
        print "Invalid coefficients. Elliptic curve does not form a group."
    else:
 
        global a
        global b
        global p
 
        a = c
        b = d
        p = e


def ec_add(x1, y1, x2, y2):

        # One or both of the points is the infinity (identy) point
    if (x1, y1)  == ('e', 'e'):
        x3 = x2
        y3 = y2

    elif x2 == 'e' and y2 == 'e':
        x3 = x1
        y3 = y1

    ################################################################

    elif x1 == x2: # The points are inverse to each other
        x3 = 'e'
        y3 = 'e'

    else:
        k = ((y2-y1)*modinv((x2-x1) % p, p)) % p

    #################################################################

    if x1 != x2: # The points are NOT inverse to each other
        x3 = (pow(k, 2) - x1 - x2) % p
        y3 = (k * (x1-x3) - y1) % p

    #################################################################

    elif x1 == x2 and y1 == y2: # The points are the same
        k = ((3*pow(x1, 2) + a)*modinv(((2*y1 % p)), p)) % p
        x3 = (pow(k, 2) - 2*x1) % p
        y3 = (k * (x1-x3) - y1) % p

    else:
        x3 = -1
        y3 = -1
    
    return (x3, y3)

 # Algorithm taken from http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python

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
        raise Exception('modular inverse does not exist')
    else:
        return x % m

    # Simple VERY INEFFICIENT primality test
def isprime(x):
    if x == 1: return False

    elif x <= 0: return False

    elif x%2 == 0: return False

    else:
        for y in range(3, x/2+1, 2):
            if x % y == 0: return False
        return True

