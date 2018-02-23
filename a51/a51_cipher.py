'''A5/1 cipher'''
#!/usr/bin/env python3
#encoding: UTF-8

from getpass import getuser

def populate_registers(init_keyword: str) -> tuple:
    '''Populate registers'''
    xyz=''
    for ch in init_keyword:
        xyz += bin(ord(ch))[2:].zfill(8)
    return (xyz[:19],xyz[19:41],xyz[41:])


def majority(x8_bit: str, y10_bit: str, z10_bit: str) -> str:
    '''Return the majority bit'''
    sumNo = int(x8_bit) + int(y10_bit) + int(z10_bit)
    if sumNo > 1:
        return 1
    else:
        return 0

def step_x(register: str) -> str:
    '''Stepping register X'''
    t = int(register[13])^int(register[16])^int(register[17])^int(register[18])
    return str(t)+register[:18]

def step_y(register: str) -> str:
    '''Stepping register Y'''
    t = int(register[20])^int(register[21])
    return str(t)+register[:21]

def step_z(register: str) -> str:
    '''Stepping register Z'''
    t = int(register[7])^int(register[20])^int(register[21])^int(register[22])
    return str(t)+register[:22]

def generate_bit(x: str, y: str, z: str) -> int:
    '''Generate a keystream bit'''
    return int(x[18])^int(y[21])^int(z[22])

def generate_keystream(plaintext: str, x: str, y: str, z: str) -> str:
    '''Generate stream of bits to match length of plaintext'''
    text = ''
    keystream = ''
    for ch in plaintext:
        text += bin(ord(ch))[2:].zfill(8)
    for i in range(0, len(text)):
        maj = majority(x[8],y[10],z[10])
        if int(x[8]) == maj:
            x = step_x(x)
        if int(y[10]) == maj:
            y = step_y(y)
        if int(z[10]) == maj:
            z = step_z(z)
        bit = generate_bit(x,y,z)
        keystream += str(bit)
    return keystream

def encrypt(plaintext: str, keystream: str) -> str:
    '''Encrypt plaintext using A5/1'''
    text = ''
    for ch in plaintext:
        text += bin(ord(ch))[2:].zfill(8)
    return bin(int(keystream,2)^int(text,2))[2:]

def main():
    '''Main function'''
    print('---A5/1 Cipher---')
    secret = 'security'
    x, y, z = populate_registers(secret)
    plaintext = getuser()  # Replace with your Luther username, if necessary
    keystream = generate_keystream(plaintext, x, y, z)
    ciphertext = encrypt(plaintext, keystream)
    print('{} | {} | {}'.format(plaintext, hex(int(keystream, 2)), hex(int(ciphertext, 2))))
    print('---Over and out---')

if __name__ == '__main__':
    main()
