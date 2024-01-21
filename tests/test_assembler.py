import unittest
from Pyssemble import *


class TestReg(unittest.TestCase):

    def test_load(self):
        Li(a2, 5).execute()
        self.assertEqual(a2.value, 5)

if __name__ == '__main__':
    unittest.main()