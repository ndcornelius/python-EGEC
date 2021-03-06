from random import randint
from encryption import GroupOperations as Group
from encryption.ModularMath import modular_sqrt

# Values obtained from http://csrc.nist.gov/publications/fips/archive/fips186-2/fips186-2.pdf
p = 6277101735386680763835789423207666416083908700390324961279  # Prime modulus
r = 6277101735386680763835789423176059013767194773182842284081  # Order of group
# s = int(0x3045ae6fc8422f64ed579528d38120eae12196d5)
# c = int(0x3099d2bbbfcb2538542dcd5fb078b6ef5f3d6fe2c745de65)
b = int(0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1)  # Constant coefficient in elliptic curve
Gx = int(0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012)  # X coordinate of generator point
Gy = int(0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811)  # Y coordinate of generator point
a = -3  # Coefficient of x^3 in the elliptic curve

Group.set_curve(a, b, p)
G = (Gx, Gy)


def generate_crypto_keys():  # El-Gamal key generation

    private_key = randint(0, r)
    public_key = Group.ec_multiply(G, private_key)

    return private_key, public_key


def ec_encrypt(m, rec_key):  # El-Gamal encryption algorithm

    k = randint(2, r-1)
    s = Group.ec_multiply(rec_key, k)

    c1 = Group.ec_multiply(G, k)
    c2 = Group.ec_add(s, m)

    return c1, c2


def ec_decrypt(encm, private_key):  # El-Gamal decryption algorithm

    c1 = encm[0]
    c2 = encm[1]

    s = Group.ec_multiply(c1, private_key)
    c2_inv = (c2[0], -c2[1])
    m = Group.ec_add(c2_inv, s)
    m = (m[0], -m[1] % p)

    return m


def encode(message):  # Maps a message to a group element
    k = 20
    m = 0

    for l in message:
        m = pow(2, 7)*m + ord(l)

    if (20*m + 20) >= p:
        s = "Message too large to encode"
        raise Exception(s)
    for i in range(1, 20):
        x = k * m + i
        c = (pow(x, 3, p) + a * x + b) % p
        y = modular_sqrt(c, p)
        if y != -1:
            return x, y
    print( "No encoding found") 


def decode(message):  # Recovers the message from the decrypted encoding

    k = 20
    x = message[0]
    plaintext = ""

    m = (x-1)//k
    length = pow(2, 7)
    while (m % length) != m:
        bin_char = m % length
        char = chr(bin_char)
        plaintext = char + plaintext
        m = (m - bin_char)//length

    plaintext = chr(m) + plaintext
    return plaintext
