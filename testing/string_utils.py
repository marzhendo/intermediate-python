import unittest
def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def is_capalized(s):
    return s[0].isupper() 

class TestStringUtils(unittest.TestCase):
    def helper_test_reverse(self, s, expected):
        result = reverse_string(s)
        self.assertEqual(result, expected)
    def helper_test_capitalize(self, s, expected):
        result = capitalize_string(s)
        self.assertEqual(result, expected)
    def helper_test_is_capitalized(self, s, expected):
        result = is_capalized(s)
        self.assertEqual(result, expected)
    def test_reverse_string(self):
        self.helper_test_reverse("hello", "olleh")
        self.helper_test_reverse("Python", "nohtyP")
    def test_capitalize_string(self):
        self.helper_test_capitalize("hello", "Hello")
        self.helper_test_capitalize("python", "Python")
    def test_is_capitalized(self):
        self.helper_test_is_capitalized("Hello", True)
        self.helper_test_is_capitalized("hello", False)
if __name__ == '__main__':
    unittest.main()

