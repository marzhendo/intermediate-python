import unittest
from test_string import huruf_terbalik, huruf_besar, apakah_berhuruf_besar

class TestStringFunctions(unittest.TestCase):
    def test_huruf_terbalik(self):
        self.assertEqual(huruf_terbalik("halo"), "olah")
        self.assertEqual(huruf_terbalik("Python"), "nohtyP")
    def test_huruf_besar(self):
        self.assertEqual(huruf_besar("halo"), "Halo")
        self.assertEqual(huruf_besar("python"), "Python")
    def test_apakah_berhuruf_besar(self):
        self.assertTrue(apakah_berhuruf_besar("Halo"))
        self.assertFalse(apakah_berhuruf_besar("halo"))
if __name__ == '__main__':
    unittest.main()