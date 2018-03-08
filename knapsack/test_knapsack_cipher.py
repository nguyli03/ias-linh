'''
Testing the Merkle–Hellman Knapsack cipher
Roman Yasinovskyy, 2018
Do not modify this file (except for removing skip decorators). If necessary, create your own tests in a separate file.
'''

#!/usr/bin/python3

import unittest
import knapsack_cipher as knapsack

class TestKnapsackCipherMethods(unittest.TestCase):
    '''Testing the Merkle–Hellman Knapsack cipher methods'''

    def setUp(self):
        '''Set up testing objects'''
        self.sik = [2, 3, 7, 14, 30, 57, 120, 251]
        self.sik2 = [1, 3, 8, 20, 49, 106, 203, 514]
        self.sik3 = [1, 3, 10, 24, 56, 106, 227, 513, 1042, 2449, 4708, 10395, 22576, 48888, 106997, 204949, 441568, 915283, 1771596, 3762909, 7923576, 16576124, 35498264, 72793824, 145879860, 288586460, 603434733, 1246270736, 2639787213, 5471972165, 11355783766, 23055631405]

    # @unittest.skip('Not implemented yet')  # Remove this line once function is implemented
    def test_generate_sik(self):
        '''Testing generate_sik function'''
        sik = knapsack.generate_sik(8)
        for i in range(len(sik)):
            self.assertGreater(sik[i], sum(sik[:i]))
        sik = knapsack.generate_sik()
        for i in range(len(sik)):
            self.assertGreater(sik[i], sum(sik[:i]))

    # @unittest.skip('Not implemented yet')  # Remove this line once function is implemented
    def test_calculate_n(self):
        '''Testing calculate_n function'''
        self.assertEqual(knapsack.calculate_n(self.sik), 485)
        self.assertEqual(knapsack.calculate_n(self.sik2), 905)
        self.assertEqual(knapsack.calculate_n(self.sik3), 44947432427)

    # @unittest.skip('Not implemented yet')  # Remove this line once function is implemented
    def test_modinv(self):
        '''Testing modinv function'''
        self.assertEqual(knapsack.modinv(self.sik, 41, 491), 12)
        self.assertEqual(knapsack.modinv(self.sik2), 18)
        self.assertEqual(knapsack.modinv(self.sik3), 37341394791)
        self.assertEqual(knapsack.modinv([], 3067, 44947432427), 37341394791)

    # @unittest.skip('Not implemented yet')  # Remove this line once function is implemented
    def test_generate_gk(self):
        '''Testing generate_gk function'''
        self.assertEqual(knapsack.generate_gk(self.sik, 41, 491), [82, 123, 287, 83, 248, 373, 10, 471])
        self.assertEqual(knapsack.generate_gk(self.sik2), [352, 151, 101, 705, 53, 207, 866, 833])

    # @unittest.skip('Not implemented yet')  # Remove this line once function is implemented
    def test_encrypt(self):
        '''Testing encrypt function'''
        gk = [82, 123, 287, 83, 248, 373, 10, 471]
        gk2 = knapsack.generate_gk(self.sik2)
        gk3 = knapsack.generate_gk(self.sik3)
        self.assertEqual(knapsack.encrypt('\x96', gk, 8), [548])
        self.assertEqual(knapsack.encrypt('LC', gk2, 8), [411, 1850])
        self.assertEqual(knapsack.encrypt('Luther', gk3), [71178494517, 383930127])
        self.assertEqual(knapsack.encrypt('Information Assurance and Security', gk3), [143686910132, 110490084383, 66501366787, 150461182644, 145232931589, 152421009503, 142249758166, 93577380330, 752089740])

    # @unittest.skip('Not implemented yet')  # Remove this line once function is implemented
    def test_decrypt(self):
        '''Testing decrypt function'''
        self.assertEqual(knapsack.decrypt([548], self.sik, 491, 12), '\x96')
        self.assertEqual(knapsack.decrypt([143686910132, 110490084383, 66501366787, 150461182644, 145232931589, 152421009503, 142249758166, 93577380330, 752089740], self.sik3), 'Information Assurance and Security')
        self.assertEqual(knapsack.decrypt([71544709652, 85040109112, 95581860118, 50908490596, 57985056401], self.sik3), 'Nothing to see here')

if __name__ == '__main__':
    unittest.main(verbosity=2)
