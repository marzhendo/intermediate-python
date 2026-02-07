"""
Edge case adalah suatu kondisi atau situasi yang terjadi pada batasan tertentu
dari suatu sistem atau fungsi. Dalam pengujian perangkat lunak, edge case sering
kali mengacu pada skenario yang jarang terjadi atau tidak biasa, yang dapat
mengungkap kelemahan atau bug dalam kode. Contoh edge case meliputi input yang
sangat besar atau sangat kecil, input yang tidak valid, atau situasi di mana
sistem beroperasi di luar batas normalnya.
"""

import unittest
from math import sqrt

def divide(a, b):
    return a / b

def get_sqrt(n):
    return sqrt(n)

class TestUnexpected(unittest.TestCase):
    def test_sqrt_positive(self):
        self.assertEqual(get_sqrt(144), 12)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            get_sqrt(-1)

    def test_divide_normal(self):
        self.assertEqual(divide(144, 12), 12)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()