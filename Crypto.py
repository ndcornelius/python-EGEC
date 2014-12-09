import ECGroupOperations as EC
from random import randint
from string import ascii_letters, digits, punctuation, whitespace

p = 6277101735386680763835789423207666416083908700390324961279 #Prime modulus
r = 6277101735386680763835789423176059013767194773182842284081 #Order of group
s = int(0x3045ae6fc8422f64ed579528d38120eae12196d5)
c = int(0x3099d2bbbfcb2538542dcd5fb078b6ef5f3d6fe2c745de65)
b = int(0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1) # Constant coefficient in elliptic curve
Gx = int(0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012) # X coordinate of generator point
Gy = int(0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811) # Y coordinate of generator point
a = -3 # Coefficient of x^3 in the elliptic curve

EC.set_curve(a, b, p)

G = (Gx, Gy)
LIBRARY = [EC.ec_multiply(G, x) for x in range(0,127)] # Message encoding library

#priv_key = 0 # Initial global declarations of public and private key
#pub_key = 0

    # El-Gamal key generation
def generate_crypto_keys():
 #   global priv_key
  #  global pub_key

    priv_key = randint(0, r)
    pub_key = EC.ec_multiply(G, priv_key)

    return (priv_key, pub_key)

    # El-Gamal encryption algorithm
def ec_encrypt(m, rec_key):

    k = randint(2, r-1)
    s = EC.ec_multiply(rec_key, k)

    c1 = EC.ec_multiply(G, k)
    c2 = EC.ec_add(s, m)

    return (c1, c2)

    # El-Gamal decryption algorithm
def ec_decrypt(encm, priv_key):

    c1 = encm[0]
    c2 = encm[1]

    s = EC.ec_multiply(c1, priv_key)
    c2_inv = (c2[0], -c2[1])
    m = EC.ec_add(c2_inv, s)
    m = (m[0], -m[1] % p)

    return m

    # Turns an ASCII character message in to an element of the Group
def encode(message):
    if message in (ascii_letters + digits + punctuation):
        y = int(ord(message))
        #print (y)
        return LIBRARY[y]
    else: return False

    # Turns an encoded message into an ASCII character
def decode(message):
    x = 0
    while message != LIBRARY[x]: 
        x += 1
        #print(str(LIBRARY[x]) + "   " + str(x) + " = " + str(chr(x)))
    return chr(x)
