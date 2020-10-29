import socket
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad,unpad
import sys

def getKeys():
    '''
    This function returns the private key of the sender 
    and the public key of the reciever.
    '''
    key = open('AlicePrivateKey.pem', 'rb').read()
    key1 = open('BobPublicKey.pem', 'rb').read()
    return RSA.importKey(key), RSA.importKey(key1)

def connectToServer():
    '''
    This function is used to establish connection to the server
    It returns  the socket created to be used later to send the message and close connection.
    '''
    HOST = socket.gethostname()
    PORT = 5555
    senderSocket = socket.socket()
    print('Connecting to server...')
    try:
        senderSocket.connect((HOST, PORT))
    except socket.error as msg:
        print ('Bind failed.') 
        sys.exit()
    return senderSocket

def sendMessage(senderSocket):
    '''
    This function takes input the message from the user and then sends
    it to the server using the senderSocket
    '''
    inputMessage = input('Enter Email:')
    #Create the hash of the inputMessage
    inputMessageHashed = SHA256.new(inputMessage.encode())
    #Signing the hashed input message using Alices's key.
    signer = PKCS1_v1_5.new(alicePrivateKey)
    aliceSignature = signer.sign(inputMessageHashed)
    #Concatenate the inputMessage and aliceSignature
    messageAndSign = inputMessage.encode() + b'\n\n\n\n\n' + aliceSignature
    #One time secret key
    key = get_random_bytes(16)
    # AES Encryption using one time secret key
    aes = AES.new(key, AES.MODE_CBC)
    encryptedMessage = aes.encrypt(pad(messageAndSign, AES.block_size))
    #Encrypting the one time secret key using Bob's public key
    rsa = PKCS1_OAEP.new(bobPublicKey)
    encryptedkey = rsa.encrypt(key)
    #Concatenate the encrypted key with encrypted inputMessage
    finalMessage = encryptedkey + b'\n\n\n\n\n' + aes.iv + b'\n\n\n\n\n' + encryptedMessage
    senderSocket.send(finalMessage)

def closeConnection(senderSocket):
    senderSocket.close()

'''
The logic of the code is simple,
first get the encryption keys
then take input from user and send it to the server
finally close the connection
'''
print("This is the sender (Alice)\n")
alicePrivateKey, bobPublicKey = getKeys() 
senderSocket = connectToServer()
sendMessage(senderSocket)
closeConnection(senderSocket)