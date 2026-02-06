"""
Docstring for testing.demo
Library unittest memiliki fungsi untuk melakukan pengujian unit pada kode Python.
ada beberapa metode penting dalam unittest yang sering digunakan, antara lain:
a. assertEqual(a, b): Memeriksa apakah nilai a sama dengan nilai b.
b. assertTrue(x): Memeriksa apakah x bernilai True.
c. assertFalse(x): Memeriksa apakah x bernilai False.
d. setUp(): Metode yang dijalankan sebelum setiap metode pengujian untuk menyiapkan kondisi awal.
e. tearDown(): Metode yang dijalankan setelah setiap metode pengujian untuk membersihkan kondisi setelah pengujian.
"""

import unittest
from test_string_lagi import panjang_string, isEmptyString, include_char, count_char

# Membuat kelas pengujian yang mewarisi dari unittest.TestCase
class TestStringLagiFunctions(unittest.TestCase):
    # Metode pengujian untuk fungsi panjang_string
    def test_panjang_string(self):
        # Memeriksa apakah panjang string "hello" adalah 5
        self.assertEqual(panjang_string("hello"), 5)
        # Memeriksa apakah panjang string kosong adalah 0
        self.assertEqual(panjang_string(""), 0)
    # Metode pengujian untuk fungsi isEmptyString
    def test_isEmptyString(self):
        # Memeriksa apakah string kosong dikenali sebagai string kosong
        self.assertTrue(isEmptyString(""))
        # Memeriksa apakah string "not empty" tidak dikenali sebagai string kosong
        self.assertFalse(isEmptyString("not empty"))
    # Metode pengujian untuk fungsi include_char
    def test_include_char(self):
        # Memeriksa apakah karakter 'e' ada dalam string "hello"
        self.assertTrue(include_char("hello", "e"))
        # Memeriksa apakah karakter 'a' tidak ada dalam string "hello"
        self.assertFalse(include_char("hello", "a"))
    # Metode pengujian untuk fungsi count_char
    def test_count_char(self):
        # Memeriksa apakah jumlah karakter 'l' dalam string "hello" adalah 2
        self.assertEqual(count_char("hello", "l"), 2)
        # Memeriksa apakah jumlah karakter 'z' dalam string "hello" adalah 0
        self.assertEqual(count_char("hello", "z"), 0)

    # Contoh penggunaan setUp dan tearDown
    def setUp(self):
        # Kode yang dijalankan sebelum setiap metode pengujian
        # Skenario: Menyiapkan data string yang akan digunakan dalam pengujian
        print("\n--- setUp: Menyiapkan kondisi awal ---")
        self.test_string = "hello world"
        self.empty_string = ""
        self.special_string = "Python Programming!"
        print(f"Data test disiapkan: '{self.test_string}', '{self.empty_string}', '{self.special_string}'")
    
    def tearDown(self):
        # Kode yang dijalankan setelah setiap metode pengujian
        # Skenario: Membersihkan/menghapus data setelah pengujian selesai
        print("--- tearDown: Membersihkan kondisi ---")
        del self.test_string
        del self.empty_string
        del self.special_string
        print("Data test dibersihkan.\n")
    
    # Metode pengujian yang menggunakan data dari setUp
    def test_with_setup_data(self):
        """Contoh test yang menggunakan data yang disiapkan di setUp"""
        # Menggunakan self.test_string yang disiapkan di setUp
        self.assertEqual(panjang_string(self.test_string), 11)  # "hello world" = 11 karakter
        self.assertTrue(include_char(self.test_string, "o"))
        self.assertEqual(count_char(self.test_string, "l"), 3)  # 3 huruf 'l' di "hello world"
        
    def test_empty_string_from_setup(self):
        """Test menggunakan empty_string dari setUp"""
        self.assertTrue(isEmptyString(self.empty_string))
        self.assertEqual(panjang_string(self.empty_string), 0)
        
    def test_special_string_from_setup(self):
        """Test menggunakan special_string dari setUp"""
        self.assertEqual(panjang_string(self.special_string), 19)  # "Python Programming!" = 19
        self.assertTrue(include_char(self.special_string, "!"))
        self.assertFalse(isEmptyString(self.special_string))

# Menjalankan pengujian jika file ini dijalankan sebagai skrip utama
if __name__ == '__main__':
    unittest.main()