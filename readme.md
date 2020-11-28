# S/MIME Protocol

This repository contains my implementation of the S/MIME protocol given to me as an assignment in the Network Security course taken at IIIT-Allahabad.

### Problem statement:
Create a simple mail server using S/MIME.

### About
SMTP, Simple Mail Transfer Protocol was first developed in 1982. It had very few security features. Therefore to include features to digitally sign, encrypt, and decrypt emails 2 new standards were developed , PGP and SMIME. The PGP (Pretty Good Privacy) and S/MIME (Secure Multipurpose Internet Mail Extensions) are the security protocols designed to serve for securing the electronic mail facility.They were introduced to add encryption/decryption and signature/verification features to SMTP (simple mail transfer protocol).
In S/MIME, the sender or receiver does not rely on exchanging keys in advance and share a common certifier on which both can rely. The user first obtains a public-private key pair from a centralized trusted authority. The private key is kept secret with the user and the public key can be distributed with others.
The email to be sent is hashed and the hashed message is signed with the sender's private key. Now this signature and the original messages is encrypted using a one time password. This one time secret key is encrypted with the receiver’s public key. Thus, only the recipient would be able to get the one time secret key to decrypt the secret message and verify the sender after encrypting the message and matching it with the recieved value. And, at the same time, no one else other than the sender would be able to modify the original message.

### Concepts/Techniques:
1. Socket Programming
2. RSA encryption
3. AES encryption
4. One time pad
5. Digital Signature
6. SHA hashing

### Getting Started

All of these codes have been done in python3. To run any of these codes, just install any necessary dependencies and compile it in any python compiler. Ensure that all the files are in the same directory.
To run this code, follow these steps:
1. Install the necessary dependencies using pip or pip3
2. Run python3 ```KeyGenerator.py``` to generate the public and private keys for Alice and Bob.
3. Run python3 ```Server.py``` in bash terminal
4. In a different terminal run python3 ```Sender.py```
5. Again in a different terminal run python3 ```Reciever.py```
6. Type in the required email in the sender terminal.
7. Observe the changes in the server and the reciever terminal.

### If this repository helped you in any way. Don't forget to :star: the repository. This helps others to reach here faster. Sharing is caring :angel:

## Built with
* [Python3](https://www.python.org/)

## Contributing

I am open to contributions. Contact me on [Facebook](https://www.facebook.com/mishraprateekaries) for any queries.

## Authors

* Prateek Mishra

See also the list of [contributors](https://github.com/MiKinshu/S-MIME-Protocol/graphs/contributors) who participated in the project.

## Acknowledgements
* I am thankful to Dr. S. Venkatesan (My NS instructor) for giving me this assignment and teaching me the basics of Network Security.