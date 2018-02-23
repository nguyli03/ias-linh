'''
Testing the A5/1 cipher
Roman Yasinovskyy, 2018
'''

#!/usr/bin/python3

import unittest
import a51_cipher as a51
from collections import namedtuple


class TestA51CipherMethods(unittest.TestCase):
    '''Testing the A5/1 cipher methods'''

    def setUp(self):
        '''Set up testing objects'''
        # Task 1
        self.x1 = '1010101010101010101'
        self.y1 = '1100110011001100110011'
        self.z1 = '11100001111000011110000'
        # Task 2
        self.x2 = '0101010101010101010'
        self.y2 = '0011001100110011001100'
        self.z2 = '00011100011100011100011'

    def test_majority(self):
        '''Testing majority function'''
        self.assertEqual(a51.majority(0, 0, 0), 0)
        self.assertEqual(a51.majority(0, 0, 1), 0)
        self.assertEqual(a51.majority(0, 1, 0), 0)
        self.assertEqual(a51.majority(0, 1, 1), 1)
        self.assertEqual(a51.majority(1, 0, 0), 0)
        self.assertEqual(a51.majority(1, 0, 1), 1)
        self.assertEqual(a51.majority(1, 1, 0), 1)
        self.assertEqual(a51.majority(1, 1, 1), 1)

    def test_populate_registers(self):
        '''Testing register population function'''
        secret = '0infosec'
        x, y, z = a51.populate_registers(secret)
        self.assertEqual(x, '0011000001101001011')
        self.assertEqual(y, '0111001100110011011110')
        self.assertEqual(z, '11100110110010101100011')

    def test_generate_bit(self):
        '''Testing bit generation'''
        self.assertEqual(a51.generate_bit(self.x1, self.y1, self.z1), 0)
        self.assertEqual(a51.generate_bit(self.x2, self.y2, self.z2), 1)

    def test_generate_keystream(self):
        '''Testing keystream generation'''
        plaintext = 'L'  # Only used to get length of the keystream
        keystream = a51.generate_keystream(plaintext, self.x1, self.y1, self.z1)
        self.assertEqual(keystream, '10000011')

    def test_encrypt_letter(self):
        '''Testing letter encryption'''
        plaintext = 'L'
        keystream = a51.generate_keystream(plaintext, self.x2, self.y2, self.z2)
        self.assertEqual(a51.encrypt(plaintext, keystream), '10101001')

    def test_encrypt_word(self):
        '''Testing word encryption'''
        plaintext = 'Luther'
        secret = '0infosec'
        x, y, z = a51.populate_registers(secret)
        keystream = a51.generate_keystream(plaintext, x, y, z)
        ciphertext = a51.encrypt(plaintext, keystream)
        self.assertEqual(hex(int(ciphertext, 2)), '0x6afa6120004d')

if __name__ == '__main__':
    unittest.main(verbosity=2)
