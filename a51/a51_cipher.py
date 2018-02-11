'''A5/1 cipher'''
#!/usr/bin/env python3
#encoding: UTF-8

from getpass import getuser

def populate_registers(init_keyword: str) -> tuple:
    '''Populate registers'''
    raise NotImplementedError

def majority(x8_bit: str, y10_bit: str, z10_bit: str) -> str:
    '''Return the majority bit'''
    raise NotImplementedError

def step_x(register: list) -> str:
    '''Stepping register X'''
    raise NotImplementedError

def step_y(register: list) -> str:
    '''Stepping register Y'''
    raise NotImplementedError

def step_z(register: list) -> str:
    '''Stepping register Z'''
    raise NotImplementedError

def generate_bit(x: list, y: list, z: list) -> int:
    '''Generate a keystream bit'''
    raise NotImplementedError

def generate_keystream(plaintext: str, x: list, y: list, z: list) -> str:
    '''Generate stream of bits to match length of plaintext'''
    raise NotImplementedError

def encrypt(plaintext: str, keystream: str) -> str:
    '''Encrypt plaintext using A5/1'''
    raise NotImplementedError

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
