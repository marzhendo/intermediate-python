import unittest
from test_string_lagi import panjang_string, isEmptyString, include_char, count_char

class TestStringLagiFunctions(unittest.TestCase):
    def test_panjang_string(self):
        self.assertEqual(panjang_string("hello"), 5)
        self.assertEqual(panjang_string(""), 0)

    def test_isEmptyString(self):
        self.assertTrue(isEmptyString(""))
        self.assertFalse(isEmptyString("not empty"))

    def test_include_char(self):
        self.assertTrue(include_char("hello", "e"))
        self.assertFalse(include_char("hello", "a"))

    def test_count_char(self):
        self.assertEqual(count_char("banana", "a"), 3)
        self.assertEqual(count_char("banana", "b"), 1)
        self.assertEqual(count_char("banana", "z"), 0)

if __name__ == '__main__':
    unittest.main()