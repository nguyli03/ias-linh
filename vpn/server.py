#!/usr/bin/env python3
#encoding: UTF-8

from socket import socket, gethostname, AF_INET, SOCK_STREAM

HOST = gethostname()
PORT = 4390

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

    while True:
        # Receive a message
        msg_in = conn.recv(1024)
        # Close the connection
        if len(msg_in) < 1:
            conn.close()
            break
        # Manipulate the message
        msg_out = 'Server says: {}'.format(msg_in.decode('utf-8')[::-1])
        # Send a response
        conn.send(msg_out.encode())

if __name__ == '__main__':
    main()
