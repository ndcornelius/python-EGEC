 from random import randint
 import math


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

     # Generates a prime between the lower bound and the upper bound
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