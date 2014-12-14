import ECGroupOperations as EC
from random import randint
from string import ascii_letters, digits, punctuation, whitespace
from math import floor

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

def encode(message):
    k = 20
    m = 0

    for l in message:
        m = pow(2, 7)*m + ord(l)

    if (20*m + 20) >= p:
        s = "Message too large to encode"
        raise Exception(s)
    for i in range(1, 20):
        x = k*m + i
        c = (pow(x, 3, p) + a*x + b) % p
        y = EC.modular_sqrt(c, p)
        if y != 0:
            #print("Success!")
            return (x,y)
    print( "No encoding found") 

def decode(message):

    k = 20
    x = message[0]
    plaintext = ""

    m = (x-1)//k
    length = pow(2, 7)
    while (m % length) != m:
        #print(bin(m))
        bin_char = m % length
      #  print( str(type(bin_char)) + str(type(m)) + str(type(length)))
        char = chr(bin_char)
        plaintext = char + plaintext
        m = (m - bin_char)//length

    plaintext = chr(m) + plaintext
    return plaintext
