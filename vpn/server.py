#!/usr/bin/env python3
#encoding: UTF-8

from socket import socket, gethostname

HOST = gethostname()
PORT = 4390

def main():
    server_sckt = socket()
    server_sckt.bind((HOST, PORT))
    print('Listening on {}:{}'.format(HOST, PORT))
    server_sckt.listen()

    conn, _ = server_sckt.accept()

    while True:
        msg_in = conn.recv(2048)
        msg_out = 'Server says {}'.format(msg_in)
        conn.send(msg_out.encode())

if __name__ == '__main__':
    main()
