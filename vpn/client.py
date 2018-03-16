#!/usr/bin/env python3
#encoding: UTF-8

from socket import socket, gethostname, AF_INET, SOCK_STREAM

HOST = gethostname()
PORT = 4390

def main():
    server_addr = gethostname()
    client_sckt = socket(AF_INET, SOCK_STREAM)
    client_sckt.connect((server_addr, PORT))

    while True:
        msg_out = input('Enter message: ')
        if msg_out == 'BYE':
            break

        client_sckt.send(msg_out.encode())
        msg_in = client_sckt.recv(2048)
        print(msg_in.decode())

if __name__ == '__main__':
    main()
