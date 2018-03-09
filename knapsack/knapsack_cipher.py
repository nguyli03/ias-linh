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
    res =[0]*size
    for i in range(0,size):
        num = sum(res[:i])+random.randint(1,100)
        res[i] = num
    return res

def calculate_n(sik: list) -> int:
    '''
    Calculate N value
    N is greater (by 1) than the sum of all members of the SIK
    '''
    return sum(sik)+1

def egcd(a: int, b: int) -> tuple:
    '''
    Extended gcd
    * Google: modular inverse python
    '''
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(sik: list, m: int = M, n: int = None) -> int:
    '''
    Part of the implementation of the Extended Euclidean algorithm
    * https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    * http://anh.cs.luc.edu/331/notes/xgcd.pdf
    * https://www.wolframalpha.com/input/?i=3067%5E-1+mod+44947432427
    '''
    if n == None:
        n = calculate_n(sik)
    g, x, y = egcd(m, n)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % n

def generate_gk(sik: list, m: int = M, n: int = None) -> list:
    '''
    Generate a general knapsack from the provided superincreasing knapsack
    m and n are optional parameters
    '''
    res = []
    if n == None:
        n = calculate_n(sik)
    for num in sik:
        res.append((num*m)%n)
    return res

def encrypt(plaintext: str, gk: list, block: int = BLOCK_SIZE) -> list:
    '''
    Encrypt a message
    1. Convert the input plaintext to a string of binary values
    2. Pad the string to the multiple of the block size
    3. In each block, multiply a value in the binary string by a corresponding member of the general knapsack
    4. Calculate the sum of the values from the previous step and add them to a list
    5. Return the list of values
    '''
    blocks = []
    bintext = ''.join(format(ord(ch),'b').zfill(8) for ch in plaintext)
    for i in range(0, len(bintext)//block+2):
        pad = bintext[block*i:block*(i+1)]
        x = list(pad)
        x = [int(i) for i in x]
        num = 0
        for i in range(0, len(x)):
            num += x[i]*gk[i]
        if num>0:
            blocks.append(num)
    return blocks

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
    if n == None:
        n = calculate_n(sik)
    if inverse == None:
        inverse = modinv(sik,n=n)
    blocks = []
    for num in ciphertext:
        sumNo = num*inverse%n
        res = [0]*len(sik)
        for i in range(len(sik)-1,-1,-1):
            if sik[i] <= sumNo:
                res[i] =1
                sumNo -= sik[i]
        blocks += res
    # print(blocks)
    bintext = ''.join(str(x) for x in blocks)
    res = ''
    # print("bintext is: "+bintext+'\n')
    # print("len of bintext is: "+str(len(bintext))+'\n')
    # print("ias is :"+(''.join(format(ord(ch),'b').zfill(8) for ch in "Information Assurance and Security"))+'\n')
    # print("len of ias is: "+str(len(''.join(format(ord(ch),'b').zfill(8) for ch in "Information Assurance and Security")))+'\n')
    for i in range(0,len(bintext),8):
        ch = bintext[i:i+8]
        if ch != '00000000':
            res += chr(int(ch, 2))
    return res

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
