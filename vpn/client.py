#!/usr/bin/env python3
#encoding: UTF-8

from socket import socket, gethostname, AF_INET, SOCK_STREAM
from diffiehellman.diffiehellman import DiffieHellman
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from aes import AESCipher
from des import DESCipher
from Crypto.Hash import SHA256

HOST = gethostname()
PORT = 4390

def aes(shared_secret,message,keylenbit):
    keylen = keylenbit//8
    key = str(shared_secret)[0:keylen]
    zeros = (len(message)//keylen+1)*keylen - len(message)
    add = ''
    for i in range(0,zeros):
        add += '0'
    message = add+message
    aes = AESCipher(key)
    encrypt = aes.encrypt(bytes(message,'utf-8'))
    msg_out = encrypt
    return msg_out

def des(shared_secret,message,keylenbit):
    keylen = keylenbit//16
    key = str(shared_secret)[0:keylen]
    zeros = (len(message)//keylen+1)*keylen - len(message)
    add = ''
    for i in range(0,zeros):
        add += '0'
    message = add+message
    des = DESCipher(key)
    encrypt = des.encrypt(bytes(message,'utf-8'))
    msg_out = encrypt
    # print("in encrypt des")
    return msg_out

def main():
    # Create a TCP socket
    client_sckt = socket(AF_INET, SOCK_STREAM)
    # Connect to the server on the same machine
    client_sckt.connect((HOST, PORT))
    # Print a status message
    print('Connected to {}:{}'.format(HOST, PORT))
    msg_out = 'ProposedCiphers: AES:[128,256] DES:[128,256] DES3:[128,256] Blowfish:[128,256,448] CAST:[64,128] ARC2:[64,128]'
    # Close the connection
    if msg_out == '\\quit':
        client_sckt.close()
        # break
    # Send a message
    client_sckt.send(msg_out.encode())
    msg_in = client_sckt.recv(4096)
    msg_in = msg_in.decode('utf-8')
    if msg_in == 'I give up':
        print('Okay, we will stop!')
        client_sckt.close()
    else:
    # Receive a response
    # if "CipherChose" in msg_in:
        res = msg_in[14:-1].split(',')
        print(res)
        keylenbit = int(res[1])
        cipher = res[0]
        # print(keylenbit)
        # print(cipher)
        alice = DiffieHellman()
        alice.generate_public_key()
        msg_out = "Alice = "+ str(alice.public_key)
        # print("Alice public key is ", alice.public_key)
        client_sckt.send(msg_out.encode())
        msg_in = client_sckt.recv(4096)
        msg_in = msg_in.decode('utf-8')

        # if "Bob = " in msg_in:
            # print("Bob in: ", msg_in)
        bobPK = msg_in.split(' = ')[1]
        alice.generate_shared_secret(int(bobPK), echo_return_key=True)

        # Read user input
        # message = input('Enter message: ')
        # print("cipher :",cipher)
        # if cipher == "'AES'":
        #     msg_out = aes(alice.shared_secret,message,keylenbit)
        # else:
        #     message = input('Enter message: ')
        message = input('Enter message: ')
        # send the list of supported cipher
        if cipher == "'AES'":
            msg_out = aes(alice.shared_secret,message,keylenbit)
            client_sckt.send(msg_out)
        elif cipher == "'DES'":
            msg_out = des(alice.shared_secret,message,keylenbit)
            client_sckt.send(msg_out)

        msg_in = client_sckt.recv(4096)
        msg_in = msg_in.decode('utf-8')

        while msg_in == 'Please enter new message':
            print('Server says: ',msg_in)
            message = input('Enter message: ')
            # Read user input
            if cipher == "'AES'":
                msg_out = aes(alice.shared_secret,message,keylenbit)
                client_sckt.send(msg_out)
            elif cipher == "'DES'":
                msg_out = des(alice.shared_secret,message,keylenbit)
                client_sckt.send(msg_out)
            else:
                print(cipher)
                print("Okay, we'll stop")
                break
            msg_in = client_sckt.recv(4096)
            msg_in = msg_in.decode('utf-8')
            # client_sckt.send(msg_out.encode())


if __name__ == '__main__':
    main()
