import sys
import socket

def connectToClients():
    '''
    This function is used to set up the connection between the server and the clients.
    It returns the senderSocket and the recieverSocket
    '''
    HOST = socket.gethostname()
    PORT1 = 5555
    PORT2 = 5556
    socketSender = socket.socket()
    socketReceiver = socket.socket()
    print('Connecting to clients')
    try:
        socketSender.bind((HOST, PORT1))
        socketReceiver.bind((HOST, PORT2))
    except socket.error as msg:
        print ('Bind failed.') 
        sys.exit()
    socketSender.listen(5)
    socketReceiver.listen(5)
    print('Socket now listening')
    (socketSender, address1) = socketSender.accept()
    (socketReceiver, address2) = socketReceiver.accept()
    return socketSender, socketReceiver

def recieveMessage(socketSender):
    '''
    This function recieves the message from the sender(Alice)
    It returns the recieved message
    '''
    return socketSender.recv(10000000)

def forwardMessage(encryptMessage, socketReceiver):
    '''
    input parameters: This function takes in 
        a. encyptMessage : This is the encrypted message recieved from Alice.
        b. socketReciever : This is the address socket of the reciever(Bob).
    This function sends the recieved messaged to Bob.
    '''
    socketReceiver.send(encryptMessage)

def closeConnection(socketSender, socketReceiver):
    '''
    Input parameters: This function takes in:
        a. socketSender : This is the address socket of the sender (Alice).
        b. socketReciever : This is the address socket of the reciever (Bob)
    This function is used to close the connection between the servers.
    '''
    socketSender.close()
    socketReceiver.close()

'''
This code sets up connection with the clients and the recieves the message from the
sender and then forwards it to the reciever.
'''

print("This is the server\n")
socketSender, socketReceiver = connectToClients()
encryptMessage = recieveMessage(socketSender)
forwardMessage(encryptMessage, socketReceiver)
closeConnection(socketReceiver, socketSender)