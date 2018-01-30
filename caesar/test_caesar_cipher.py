'''
Testing the Caesar cipher
Roman Yasinovskyy, 2018
'''

#!/usr/bin/python3

import unittest
import caesar_cipher as cc


class TestCaesarCipherMethods(unittest.TestCase):
    '''Testing the Caesar cipher methods'''

    def test_shift_by_n(self):
        '''Testing shift_by_n() method'''
        self.assertEqual(cc.shift_by_n('hello', 3, 1), 'khoor')
        self.assertEqual(cc.shift_by_n('ZRUOG', 3, -1), 'WORLD')

    def test_encrypt(self):
        '''Testing encrypt() method'''
        self.assertEqual(cc.encrypt('hello', 3), 'KHOOR')
        self.assertEqual(cc.encrypt('hello world!', 3), 'KHOOR ZRUOG!')
        self.assertEqual(cc.encrypt('hello world', 3, True), 'KHOORZRUOG')

    def test_decrypt(self):
        '''Testing decrypt() method'''
        self.assertEqual(cc.decrypt('ZRUOG', 3), 'world')
        self.assertEqual(cc.decrypt('KHOOR ZRUOG!', 3), 'hello world')

if __name__ == '__main__':
    unittest.main(verbosity=2)
