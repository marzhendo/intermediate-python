import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a * b


class TestAddition(unittest.TestCase):
    def assert_multiply(self, a, b, expected):
        result = multiply(a, b)
        self.assertEqual(result, expected)

    def test_add(self):
        result = add(2, 3)
        expected_result = 5
        self.assertEqual(result, expected_result)

class TestSubtraction(unittest.TestCase):
    def test_subtract(self):
        result = subtract(5, 3)
        expected_result = 2
        self.assertEqual(result, expected_result)

class TestMultiplication(unittest.TestCase):
    def test_multiply(self):
        result = multiply(2, 6)
        expected_result = 12
        self.assertEqual(result, expected_result)
    
    def test_zero(self):
        self.assert_multiply(0, 5, 0)
        

    def test_negative(self):
        self.assert_multiply(-2, 3, -6)
    
    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            multiply("2", 3)

if __name__ == '__main__':
    unittest.main()