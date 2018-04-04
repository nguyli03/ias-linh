#!/usr/bin/env python3
#encoding: UTF-8

from socket import socket, gethostname, AF_INET, SOCK_STREAM
import random
import ast
from diffiehellman.diffiehellman import DiffieHellman
import Crypto.Cipher
from aes import AESCipher
from des import DESCipher

HOST = gethostname()
PORT = 4390
def aes(shared_secret,message,keylenbit):
    keylen = keylenbit//8
    key = str(shared_secret)[0:keylen]
    aes = AESCipher(key)
    decrypt = aes.decrypt(message).decode('utf-8').strip('0')
    return decrypt

def des(shared_secret,message,keylenbit):
    keylen = keylenbit//16
    key = str(shared_secret)[0:keylen]
    des = DESCipher(key)
    decrypt = des.decrypt(message).decode('utf-8').strip('0')
    # print('in decrypt des')
    return decrypt

def hash(message):
    hash = SHA256.new()
    hash.update(message)
    return hash.digest()

def main():
    # Create a TCP soclet
    server_sckt = socket(AF_INET, SOCK_STREAM)
    # Bind the program to a port
    server_sckt.bind((HOST, PORT))
    # Become a server socket
    server_sckt.listen(5)
    # Print a status message
    print('Listening on {}:{}'.format(HOST, PORT))
    # Accept a connection
    conn, client = server_sckt.accept()
    print('Connected to {}:{}'.format(client[0], client[1]))
    msg_in = conn.recv(4096)
    msg_in = msg_in.decode('utf-8')
    # Close the connection
    if len(msg_in) < 1:
        conn.close()
        # break
    # print(msg_in)
    # Manipulate the message
    # msg_out = 'Server says: {}'.format(msg_in.decode('utf-8')[::-1])
    # pick a cipher and send a message with a chosen cipher
    # if "ProposedCiphers" in msg_in:
        # will be used later
    ciphers = msg_in[15:]
    ciphers = ciphers.split(' ')
    choiceC = 'T.T'
    choiceK = 0
    for cipher in ciphers:
        if 'AES' in cipher and choiceC == 'T.T':
            choiceC = 'AES'
            keylen = ast.literal_eval(random.choice(ciphers).split(':')[1])
            if 128 in keylen:
                choiceK = 128
            elif 256 in keylen:
                choiceK = 256
            else:
                choiceK = 0
        elif 'DES' in cipher and choiceC == 'T.T':
            choiceC = 'DES'
            keylen = ast.literal_eval(random.choice(ciphers).split(':')[1])
            if 128 in keylen:
                choiceK = 128
            elif 256 in keylen:
                choiceK = 256
            else:
                choiceK = 0
    if choiceC =='T.T' or choiceK == 0:
        msg_out = 'I give up!'
        print(msg_out)
    else:
        msg_out = "CipherChose: "+str((choiceC,choiceK))
        print(msg_out)
        conn.send(msg_out.encode())
        msg_in = conn.recv(4096)
        msg_in = msg_in.decode('utf-8')

        # if "Alice = " in msg_in:
        # generate DH public key:
        bob = DiffieHellman()
        bob.generate_public_key()

        msg_out = 'Bob = '+ str(bob.public_key)
        # print("Bob out: ", msg_out)
        conn.send(msg_out.encode())
        alicePK = msg_in.split(' = ')[1]
        bob.generate_shared_secret(int(alicePK), echo_return_key=True)
        msg_in = conn.recv(4096)
        # msg_in = msg_in.decode('utf-8')

        if choiceC == 'AES':
            decrypt = aes(bob.shared_secret,msg_in,choiceK)
            print(decrypt)
            msg_out = "Please enter new message"
        elif choiceC == 'DES':
            decrypt = des(bob.shared_secret,msg_in,choiceK)
            print(decrypt)
            msg_out = "Please enter new message"
        else:
            msg_out = "We don't know what to do"
        conn.send(msg_out.encode())
        msg_in = conn.recv(4096)
        print(msg_in)
        while len(msg_in)>1:
            if choiceC == 'AES':
                decrypt = aes(bob.shared_secret,msg_in,choiceK)
                print(decrypt)
                msg_out = "Please enter new message"
            elif choiceC == 'DES':
                decrypt = des(bob.shared_secret,msg_in,choiceK)
                print(decrypt)
                msg_out = "Please enter new message"
            else:
                msg_out = "We don't know what to do"
            conn.send(msg_out.encode())
            msg_in = conn.recv(4096)
            # msg_in = msg_in.decode('utf-8')

    # if "Message " in msg_in:
    #     # print(msg_in)
    #     # keylen = keylenbit//8
    #     keylen = 128//8
    #     key = str(bob.shared_secret)[0:keylen]
    #     aes = AESCipher(key)
    #     message =  msg_in.strip('Message ')
    #     print(msg_in.strip('Message '))
    #     print(len(message))
    #     decrypt = aes.decrypt(message)
    #     print(decrypt)

    # while True:
    #     Receive a message


if __name__ == '__main__':
    main()

# use python crypto package and Diffie Hellman python package
