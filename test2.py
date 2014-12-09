import Crypto
import ECGroupOperations as EC

alice_keys = Crypto.generate_crypto_keys()
print ( "Keys:\nPrivate key: %s\nPublic key: %s\n" % (str(alice_keys[0]), str(alice_keys[1])))

#bob_keys = Crypto.generate_crypto_keys()

#print ( "Bob's Keys:\nPrivate key: %s\nPublic key: %s\n" % (str(bob_keys[0]), str(bob_keys[1])))

while True
    message = input("Enter the message to encrypt (Message must be a single ASCII character, no whitespace): ")

    P = message

    m = Crypto.encode(P)
print ( "Message e: %s\nEncoded message: %s" % (P, str(m)))
c = Crypto.ec_encrypt(m, bob_keys[1])

print ( "Encrypted message: %s\n" % (str(c)))

d = Crypto.ec_decrypt(c, bob_keys[0])
e = Crypto.decode(d)

print ( "Decrypted message: %s\nDecoded message: %s\n" % (str(d), str(e)))


