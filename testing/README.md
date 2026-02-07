# 📂 Testing - Panduan Unit Testing Python

Folder ini berisi materi pembelajaran tentang **Unit Testing** menggunakan library `unittest` bawaan Python. Berikut adalah evaluasi dan konsep yang dipelajari dari setiap file.

---

## 📚 Daftar Isi

- [Konsep Utama](#-konsep-utama)
- [Evaluasi File](#-evaluasi-file)
- [Assertion Methods](#-assertion-methods)
- [Best Practices](#-best-practices)
- [Kesimpulan](#-kesimpulan)

---

## 🎯 Konsep Utama

### 1. Struktur Dasar Unit Test

```python
import unittest

class TestClassName(unittest.TestCase):
    def setUp(self):
        # Dijalankan sebelum SETIAP test method
        pass
    
    def tearDown(self):
        # Dijalankan setelah SETIAP test method
        pass
    
    def test_nama_method(self):
        # Test case - harus diawali dengan 'test_'
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
```

### 2. Prinsip Unit Testing

- **Isolated**: Setiap test harus independen
- **Repeatable**: Hasil konsisten setiap kali dijalankan
- **Self-validating**: Test menentukan sendiri pass/fail
- **Fast**: Test harus cepat dieksekusi

---

## 📁 Evaluasi File

### [testing.py](testing.py)
**Konsep:** Pengenalan dasar unit testing

| Aspek | Detail |
|-------|--------|
| Fungsi yang diuji | `add()`, `subtract()`, `multiply()` |
| Assertion digunakan | `assertEqual`, `assertRaises` |
| Fitur khusus | Type validation dengan `TypeError` |
| Pembelajaran | Pengujian operasi matematika dasar dan handling tipe data |

```python
# Contoh type validation
def multiply(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a * b
```

---

### [testing2.py](testing2.py)
**Konsep:** Unit testing sederhana dengan penamaan Indonesia

| Aspek | Detail |
|-------|--------|
| Fungsi yang diuji | `kali()` (perkalian) |
| Assertion digunakan | `assertEqual` |
| Catatan khusus | ⚠️ Test `test_input_ngawur` akan fail karena fungsi tidak handle error |

**Evaluasi:** File ini menunjukkan pentingnya defensive programming - test mengharapkan `"Error"` tapi fungsi tidak menangani input string.

---

### [bankAkun.py](bankAkun.py)
**Konsep:** Testing class dengan business logic

| Aspek | Detail |
|-------|--------|
| Class yang diuji | `BankAccount` |
| Methods | `deposit()`, `withdraw()` |
| Assertion digunakan | `assertEqual`, `assertRaises` |
| Fitur khusus | `setUp()` dan `tearDown()` |
| Edge cases | Deposit/withdraw negatif, insufficient funds |

**Highlights:**
- Validasi input dengan `ValueError`
- Pattern: Test happy path dan error path
- Penggunaan context manager untuk assertRaises:
```python
with self.assertRaises(ValueError):
    self.account.withdraw(200)  # Insufficient funds
```

---

### [coffee_menu.py](coffee_menu.py) & [test_coffe_menu.py](test_coffe_menu.py)
**Konsep:** Testing lengkap dengan berbagai edge cases

| Aspek | Detail |
|-------|--------|
| Class yang diuji | `CoffeeMenu` |
| Methods | `get_price()`, `add_item()` |
| Total test cases | 20+ test methods |

**Test Coverage yang dipelajari:**

| Kategori | Test Cases |
|----------|------------|
| Functionality | get_price, add_item, update_item |
| Edge Cases | empty string, None, numeric names |
| Boundary | negative price, zero price, large numbers |
| Data Integrity | menu integrity, case sensitivity |
| Precision | float precision dengan `assertAlmostEqual` |

**Highlight - Comprehensive Testing:**
```python
def test_float_precision(self):
    self.coffee_menu.add_item('test float', 2.3333333)
    self.assertAlmostEqual(self.coffee_menu.get_price('test float'), 2.3333333)

def test_special_characters_in_item(self):
    self.coffee_menu.add_item('café mocha!', 3.50)
    self.assertEqual(self.coffee_menu.get_price('café mocha!'), 3.50)
```

---

### [string_utils.py](string_utils.py)
**Konsep:** Helper methods dalam test class

| Aspek | Detail |
|-------|--------|
| Fungsi yang diuji | `reverse_string()`, `capitalize_string()`, `is_capalized()` |
| Pattern | Helper test methods untuk reusability |

**Pattern Pembelajaran:**
```python
def helper_test_reverse(self, s, expected):
    result = reverse_string(s)
    self.assertEqual(result, expected)

def test_reverse_string(self):
    self.helper_test_reverse("hello", "olleh")
    self.helper_test_reverse("Python", "nohtyP")
```

---

### [test_string.py](test_string.py) & [test_string_lagi.py](test_string_lagi.py)
**Konsep:** Fungsi utility string untuk ditest

| File | Fungsi |
|------|--------|
| test_string.py | `huruf_terbalik()`, `huruf_besar()`, `apakah_berhuruf_besar()` |
| test_string_lagi.py | `panjang_string()`, `isEmptyString()`, `include_char()`, `count_char()` |

---

### [coba_test_string.py](coba_test_string.py) & [coba_test_string_lagi.py](coba_test_string_lagi.py)
**Konsep:** Implementasi test untuk string functions

**Assertion yang dipelajari:**
- `assertEqual()` - perbandingan nilai
- `assertTrue()` - kondisi boolean true
- `assertFalse()` - kondisi boolean false

---

### [demo.py](demo.py)
**Konsep:** Demo komprehensif dengan penjelasan lengkap

**Fitur yang dijelaskan:**
1. **Docstring** untuk dokumentasi test
2. **setUp()** - Menyiapkan kondisi awal
3. **tearDown()** - Membersihkan setelah test
4. **Komentar** yang menjelaskan setiap langkah

**Best Practice dari demo.py:**
```python
def setUp(self):
    print("\n--- setUp: Menyiapkan kondisi awal ---")
    self.test_string = "hello world"
    self.empty_string = ""
    self.special_string = "Python Programming!"

def tearDown(self):
    print("--- tearDown: Membersihkan kondisi ---")
    del self.test_string
    del self.empty_string
    del self.special_string
```

---

### [unexpected.py](unexpected.py)
**Konsep:** Edge Cases & Exception Testing

| Aspek | Detail |
|-------|--------|
| Fungsi yang diuji | `divide()`, `get_sqrt()` |
| Exception handled | `ZeroDivisionError`, `ValueError` |

**Definisi Edge Case:**
> Kondisi atau situasi yang terjadi pada batasan tertentu dari suatu sistem atau fungsi. Sering mengungkap kelemahan atau bug dalam kode.

**Contoh:**
```python
def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        divide(10, 0)

def test_sqrt_negative(self):
    with self.assertRaises(ValueError):
        get_sqrt(-1)
```

---

### [catatan.md](catatan.md) & [unitest.md](unitest.md)
**Konsep:** Cheat sheet untuk assertion methods

**Referensi cepat - lihat file untuk detail lengkap.**

---

## ✅ Assertion Methods

| Assertion | Kegunaan | Contoh |
|-----------|----------|--------|
| `assertEqual(a, b)` | Nilai sama persis | `self.assertEqual(result, 10)` |
| `assertNotEqual(a, b)` | Nilai berbeda | `self.assertNotEqual(score, 0)` |
| `assertTrue(x)` | Kondisi True | `self.assertTrue(is_valid)` |
| `assertFalse(x)` | Kondisi False | `self.assertFalse(is_logged_in)` |
| `assertIsNone(x)` | Nilai adalah None | `self.assertIsNone(result)` |
| `assertIsNotNone(x)` | Nilai bukan None | `self.assertIsNotNone(user)` |
| `assertRaises(Error)` | Memunculkan exception | `with self.assertRaises(ValueError):` |
| `assertIn(a, b)` | a ada dalam b | `self.assertIn("admin", roles)` |
| `assertNotIn(a, b)` | a tidak ada dalam b | `self.assertNotIn("guest", roles)` |
| `assertIs(a, b)` | Object identity sama | `self.assertIs(obj1, obj2)` |
| `assertAlmostEqual(a, b)` | Float precision | `self.assertAlmostEqual(result, 2.333)` |
| `assertGreater(a, b)` | a > b | `self.assertGreater(score, 60)` |
| `assertLess(a, b)` | a < b | `self.assertLess(value, 100)` |
| `assertRegex(text, pattern)` | Match regex | `self.assertRegex(email, r".+@.+")` |

---

## 💡 Best Practices

### 1. Naming Convention
- Test class: `Test` + nama class/fungsi yang diuji
- Test method: `test_` + deskripsi behavior yang diuji

### 2. Test Structure (AAA Pattern)
```python
def test_deposit(self):
    # Arrange - persiapan
    account = BankAccount(100)
    
    # Act - eksekusi
    account.deposit(50)
    
    # Assert - verifikasi
    self.assertEqual(account.balance, 150)
```

### 3. setUp & tearDown
- `setUp()`: Inisialisasi resources yang dibutuhkan setiap test
- `tearDown()`: Cleanup resources setelah test (mencegah memory leak)

### 4. Test Coverage Checklist
- ✅ Happy path (normal behavior)
- ✅ Edge cases (boundary values)
- ✅ Error cases (exception handling)
- ✅ Invalid inputs
- ✅ Empty inputs
- ✅ Type validation

### 5. Hindari
- ❌ `self.assertTrue(a == b)` → ✅ `self.assertEqual(a, b)`
- ❌ `self.assertEqual(result, None)` → ✅ `self.assertIsNone(result)`
- ❌ Test yang bergantung pada test lain

---

## 📝 Kesimpulan

Folder ini mencakup pembelajaran komprehensif tentang **Unit Testing Python**:

| Topik | Status |
|-------|--------|
| Struktur dasar unittest | ✅ |
| Assertion methods | ✅ |
| setUp & tearDown | ✅ |
| Exception testing | ✅ |
| Edge case handling | ✅ |
| Helper methods | ✅ |
| Type validation | ✅ |
| Float precision | ✅ |

**Rekomendasi untuk belajar lebih lanjut:**
1. `pytest` - Framework testing yang lebih modern
2. `mock` - Untuk mocking dependencies
3. Coverage tools - Untuk mengukur test coverage

---

## 🚀 Menjalankan Test

```bash
# Jalankan semua test dalam satu file
python -m unittest testing.py

# Jalankan dengan verbose output
python -m unittest -v bankAkun.py

# Jalankan test spesifik
python -m unittest testing.TestMultiplication.test_multiply
```

---

*Dibuat sebagai dokumentasi pembelajaran Unit Testing Python*
