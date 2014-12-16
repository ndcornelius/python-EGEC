from encryption import CryptographicOperations as Crypto

alice_keys = Crypto.generate_crypto_keys()
print("Keys:\nPrivate key: %s\n\nPublic key: %s\n" % (str(alice_keys[0]), str(alice_keys[1])))

bob_keys = Crypto.generate_crypto_keys()

#print ( "Bob's Keys:\nPrivate key: %s\nPublic key: %s\n" % (str(bob_keys[0]), str(bob_keys[1])))

message = input("Enter message: ")
print()

P = message

m = Crypto.encode(P)
print("\nEncoded message: %s\n" % (str(m)))

c = Crypto.ec_encrypt(m, bob_keys[1])
print("Encrypted message: %s\n" % (str(c)))

d = Crypto.ec_decrypt(c, bob_keys[0])
e = Crypto.decode(d)
print("Decrypted message: %s\n\nDecoded message: %s\n" % (str(d), str(e)))


