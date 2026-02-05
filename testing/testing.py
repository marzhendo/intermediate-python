import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        expected_result = 5
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()