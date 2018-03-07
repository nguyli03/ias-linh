'''Merkle–Hellman Knapsack cipher'''
#!/usr/bin/env python3

import math
import random

BLOCK_SIZE = 32  # 4 bytes
M = 3067  # 439th prime number, guaranteed to be relatively prime with any N

def generate_sik(size: int = BLOCK_SIZE) -> list:
    '''
    Generate a superincreasing knapsack of the specified size
    Every member in the SIK is greater than the sum of all previous members
    '''
    raise NotImplementedError

def calculate_n(sik: list) -> int:
    '''
    Calculate N value
    N is greater (by 1) than the sum of all members of the SIK
    '''
    raise NotImplementedError

def egcd(a: int, b: int) -> tuple:
    '''
    Extended gcd
    * Google: modular inverse python
    '''
    raise NotImplementedError

def modinv(sik: list, m: int = M, n: int = None) -> int:
    '''
    Part of the implementation of the Extended Euclidean algorithm
    * https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    * http://anh.cs.luc.edu/331/notes/xgcd.pdf
    * https://www.wolframalpha.com/input/?i=3067%5E-1+mod+44947432427
    '''
    raise NotImplementedError

def generate_gk(sik: list, m: int = M, n: int = None) -> list:
    '''
    Generate a general knapsack from the provided superincreasing knapsack
    m and n are optional parameters
    '''
    raise NotImplementedError

def encrypt(plaintext: str, gk: list, block: int = BLOCK_SIZE) -> list:
    '''
    Encrypt a message
    1. Convert the input plaintext to a string of binary values
    2. Pad the string to the multiple of the block size
    3. In each block, multiply a value in the binary string by a corresponding member of the general knapsack
    4. Calculate the sum of the values from the previous step and add them to a list
    5. Return the list of values
    '''
    raise NotImplementedError

def decrypt(ciphertext: list, sik: list, n: int = None, inverse: int = None, block: int = BLOCK_SIZE) -> str:
    '''
    Decrypt a message
    1. Calculate n if necessary
    2. Calculate modular inverse if necessary
    3. For every number in the ciphertex list
      1. Find the sum to solve
      2. Solve the SIK for that sum building a binary string
      3. Split that block into individual bytes
      4. Convert each byte value to a string
      5. Trim trailing 0s if necessary
    4. Return the resulting string
    '''
    raise NotImplementedError


def main():
    '''
    Main function
    Use your own values to check that functions work as expected
    Reminder: I will not run this file
    '''
    plaintext = 'Hi there'  # You may start with a single character
    sik = generate_sik()  # You may hard-code SIK as well
    # print('SIK: {}'.format(sik))
    gk = generate_gk(sik)
    # print('GK: {}'.format(gk))
    print('M: {:>24d}'.format(M))
    n = calculate_n(sik)
    print('N: {:>31d}'.format(n))
    i = modinv(sik)
    print('Inverse: {:>25d}'.format(i))
    print('m * i % n = {:>12d}'.format(M * i % n))
    ciphertext = encrypt(plaintext.strip(), gk)
    print('Plaintext: {:>20s}'.format(plaintext))
    print('Ciphertext: {}'.format(ciphertext))
    print('Decrypted: {:>20s}'.format(decrypt(ciphertext, sik)))

if __name__ == '__main__':
    main()
