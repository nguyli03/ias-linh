'''
Testing the VPN Client
Roman Yasinovskyy, 2018
'''

#!/usr/bin/python3

import unittest
from server import *

class TestClientMethods(unittest.TestCase):
    '''Testing the VPN Client'''

    def setUp(self):
        '''Set up testing objects'''
        self.foo = 439

    def test_1(self):
        '''Testing something'''
        assert True

    def test_2(self):
        '''Testing something'''
        assert False

if __name__ == '__main__':
    unittest.main(verbosity=2)
