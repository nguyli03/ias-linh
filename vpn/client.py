#!/usr/bin/env python3
#encoding: UTF-8

from socket import socket, gethostname, AF_INET, SOCK_STREAM

HOST = gethostname()
PORT = 4390

def main():
    # Create a TCP socket
    client_sckt = socket(AF_INET, SOCK_STREAM)
    # Connect to the server on the same machine
    client_sckt.connect((HOST, PORT))
    # Print a status message
    print('Connected to {}:{}'.format(HOST, PORT))

    while True:
        # Read user input
        msg_out = input('Enter message: ')
        # Close the connection
        if msg_out == '\\quit':
            client_sckt.close()
            break
        # Send a message
        client_sckt.send(msg_out.encode())
        # Receive a response
        msg_in = client_sckt.recv(1024)
        # Print the response
        print(msg_in.decode('utf-8'))

if __name__ == '__main__':
    main()
