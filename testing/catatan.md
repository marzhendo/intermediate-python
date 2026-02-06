# Unit Test Assertions dalam Python

## ✅ Assertions untuk Perbandingan Nilai

### 1. `assertEqual(a, b)`
**Penggunaan:** Memeriksa apakah dua nilai persis sama
```python
self.assertEqual(multiply(2, 3), 6)
```
**Kapan digunakan:**
- Hasil harus persis sama
- Paling umum digunakan

**Hindari:**
- Menggunakan untuk cek kondisi (gunakan `assertTrue`)

---

### 2. `assertNotEqual(a, b)`
**Penggunaan:** Memeriksa apakah dua nilai berbeda
```python
self.assertNotEqual(result, 0)
```
**Kapan digunakan:**
- Memastikan hasil tidak sama
- Regression test

---

## 🔍 Assertions untuk Kondisi Boolean

### 3. `assertTrue(expr)`
**Penggunaan:** Memeriksa apakah ekspresi bernilai `True`
```python
self.assertTrue(is_valid)
```
**Kapan digunakan:**
- Kondisi logika
- Return `True` / `False`

**❌ HINDARI:** `self.assertTrue(a == b)` → **Gunakan:** `self.assertEqual(a, b)`

---

### 4. `assertFalse(expr)`
**Penggunaan:** Kebalikan dari `assertTrue`
```python
self.assertFalse(is_logged_in)
```

---

## ⚠️ Assertions untuk Error

### 5. `assertRaises(ErrorType)`
**Penggunaan:** Memastikan fungsi mengeluarkan error yang spesifik
```python
with self.assertRaises(TypeError):
    multiply("2", 3)
```
**Kapan digunakan:**
- Validasi input
- Defensive programming

---

## 📦 Assertions untuk Koleksi

### 6. `assertIn(item, collection)`
```python
self.assertIn("admin", roles)
```

### 7. `assertNotIn(item, collection)`
```python
self.assertNotIn("guest", roles)
```
**Catatan:** Lebih ekspresif daripada `assertTrue(x in y)`

---

## 🎯 Assertions untuk Object Identity

### 8. `assertIs(a, b)`
**Penggunaan:** Memeriksa apakah dua reference menunjuk ke object yang sama
```python
self.assertIs(obj1, obj2)
```
**Kapan digunakan:**
- Singleton
- Caching
- Object identity

---

### 9. `assertIsNone(x)` & `assertIsNotNone(x)`
```python
self.assertIsNone(result)
```
**Catatan:** Lebih bersih daripada `self.assertEqual(result, None)`

---

## 🔢 Assertions untuk Angka

### 10. Perbandingan Nilai Numerik
```python
self.assertGreater(score, 60)
self.assertLess(value, 100)
self.assertGreaterEqual(score, 60)
self.assertLessEqual(value, 100)
```
**Kapan digunakan:**
- Score/rating
- Limit/threshold
- Range validation

---

## 🧪 Assertions untuk String & Regex

### 11. `assertRegex(text, pattern)`
```python
self.assertRegex(email, r".+@.+\..+")
```
**Kapan digunakan:**
- Validasi format
- Log output validation
