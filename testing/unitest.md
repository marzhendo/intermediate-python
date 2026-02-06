# 🧪 Python unittest – Assertion Cheat Sheet

Cheat sheet pribadi untuk memilih **assertion yang tepat sesuai niat test**.

---

## 🟢 Assertion Paling Umum

### `assertEqual(a, b)`

**Nilai harus sama persis**

```python
self.assertEqual(result, 10)
```

Dipakai untuk:

* hasil perhitungan
* return value pasti

---

### `assertNotEqual(a, b)`

**Nilai tidak boleh sama**

```python
self.assertNotEqual(score, 0)
```

Dipakai untuk:

* memastikan ada perubahan
* regression test

---

## 🔵 Boolean Assertion

### `assertTrue(expr)`

```python
self.assertTrue(is_valid)
```

Dipakai jika function **return True**

---

### `assertFalse(expr)`

```python
self.assertFalse(is_logged_in)
```

Dipakai jika function **return False**

---

## 🟣 None & Existence

### `assertIsNone(x)`

```python
self.assertIsNone(user)
```

Dipakai jika **return harus None**

---

### `assertIsNotNone(x)`

```python
self.assertIsNotNone(user)
```

Dipakai jika **return tidak boleh None**

---

## 🔴 Error / Exception

### `assertRaises(ErrorType)`

```python
with self.assertRaises(TypeError):
    multiply("2", 3)
```

Dipakai untuk:

* validasi input
* guard clause
* defensive programming

---

## 🟡 Collection (list, set, dict)

### `assertIn(item, collection)`

```python
self.assertIn("admin", roles)
```

### `assertNotIn(item, collection)`

```python
self.assertNotIn("admin", roles)
```

---

## 🟠 Object Identity

### `assertIs(a, b)`

```python
a = []
b = a
self.assertIs(a, b)
```

Dipakai jika:

* object harus **sama di memory**
* singleton
* cache

---

## 🟤 Number Comparison

### `assertGreater(a, b)`

```python
self.assertGreater(score, 60)
```

Tersedia juga:

* `assertLess`
* `assertGreaterEqual`
* `assertLessEqual`

---

## 🟢 String & Regex

### `assertRegex(text, pattern)`

```python
self.assertRegex(email, r".+@.+\\..+")
```

Dipakai untuk:

* validasi format
* log output

---

## 🧠 Pola Hafalan Cepat

| Tujuan      | Assertion                  |
| ----------- | -------------------------- |
| Sama nilai  | `assertEqual`              |
| Boolean     | `assertTrue / assertFalse` |
| None        | `assertIsNone`             |
| Error       | `assertRaises`             |
| Ada di list | `assertIn`                 |
| Tidak ada   | `assertNotIn`              |
| Object sama | `assertIs`                 |

---

