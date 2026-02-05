import unittest

def kali(a, b):
    return a * b

class TestMultiplication(unittest.TestCase):
    def test_kali(self):
        result = kali(3, 5)
        expected_result = 15
        self.assertEqual(result, expected_result)
    def test_negatif(self):
        result = kali(-2, 10)
        expected_result = -20
        self.assertEqual(result, expected_result)
    def test_input_ngawur(self):
        result = kali (3, "Budi")
        expected_result = "Error"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()