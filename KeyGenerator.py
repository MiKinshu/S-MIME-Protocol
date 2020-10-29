from Crypto.PublicKey import RSA
from Crypto import Random
#using these packages from the pycrytodome library.

'''
Now we are generating public and private keys for both Alice and Bob.
The keys would be stored in the same directory as the code.
'''
randomNumber = Random.new().read
keys = RSA.generate(1024, randomNumber)
file = open('AlicePrivateKey.pem', 'wb')
file.write(keys.exportKey('PEM'))
file.close()
file = open('AlicePublicKey.pem', 'wb')
file.write(keys.publickey().exportKey('PEM'))
file.close()

keys = RSA.generate(1024, randomNumber)
file = open('BobPrivateKey.pem', 'wb')
file.write(keys.exportKey('PEM'))
file.close()
file = open('BobPublicKey.pem', 'wb')
file.write(keys.publickey().exportKey('PEM'))
file.close()