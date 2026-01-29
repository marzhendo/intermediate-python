# 📚 Python Data Structures

# Struktur Data Python

Dokumentasi lengkap tentang struktur data bawaan Python, termasuk kapan dan bagaimana menggunakannya dengan tepat.

---

## 📋 Daftar Isi / Table of Contents

1. [Overview](#overview)
2. [List](#1-list)
3. [Tuple](#2-tuple)
4. [Set](#3-set)
5. [Dictionary](#4-dictionary)
6. [Perbandingan / Comparison](#perbandingan--comparison)
7. [Kapan Menggunakan? / When to Use?](#kapan-menggunakan--when-to-use)

---

## Overview

Python memiliki 4 struktur data built-in utama:

| Struktur Data  | Mutable  | Ordered  | Duplicates | Syntax      |
| -------------- | -------- | -------- | ---------- | ----------- |
| **List**       | ✅ Ya    | ✅ Ya    | ✅ Ya      | `[1, 2, 3]` |
| **Tuple**      | ❌ Tidak | ✅ Ya    | ✅ Ya      | `(1, 2, 3)` |
| **Set**        | ✅ Ya    | ❌ Tidak | ❌ Tidak   | `{1, 2, 3}` |
| **Dictionary** | ✅ Ya    | ✅ Ya\*  | Keys: ❌   | `{"a": 1}`  |

> \*Dictionary ordered sejak Python 3.7+

---

## 1. List

### Definisi / Definition

List adalah koleksi data yang **ordered** (terurut), **mutable** (dapat diubah), dan **mengizinkan duplikat**.

```python
# Membuat list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
```

### ✅ Best Practices

| Situasi                    | Gunakan List Ketika...                              |
| -------------------------- | --------------------------------------------------- |
| **Koleksi Dinamis**        | Anda perlu menambah/menghapus elemen secara berkala |
| **Urutan Penting**         | Posisi elemen dalam koleksi memiliki makna          |
| **Duplikat Diperbolehkan** | Data yang sama bisa muncul lebih dari sekali        |
| **Iterasi Berurutan**      | Anda perlu mengakses data secara berurutan          |

### 🎯 Use Cases

```python
# 1. Shopping Cart - item bisa ditambah/dihapus
shopping_cart = []
shopping_cart.append("iPhone")
shopping_cart.append("MacBook")
shopping_cart.remove("iPhone")

# 2. History/Log - mencatat urutan kejadian
browser_history = []
browser_history.append("google.com")
browser_history.append("github.com")

# 3. Queue/Stack sederhana
stack = []
stack.append(1)  # push
stack.pop()      # pop

# 4. Menyimpan hasil query database
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]
```

### ⚠️ Kapan TIDAK Menggunakan List

```python
# ❌ JANGAN: Untuk data yang tidak boleh berubah
DAYS_OF_WEEK = ["Mon", "Tue", "Wed"]  # Gunakan tuple

# ❌ JANGAN: Untuk cek keanggotaan besar
large_list = [1, 2, 3, ..., 1000000]
if 500000 in large_list:  # O(n) - lambat!
    pass
# ✅ Gunakan set untuk pencarian cepat
```

### 📌 Methods Penting

```python
fruits = ["apple", "banana"]

# Menambah elemen
fruits.append("cherry")      # Di akhir
fruits.insert(0, "mango")    # Di posisi tertentu
fruits.extend(["grape"])     # Gabung list

# Menghapus elemen
fruits.remove("banana")      # Berdasarkan nilai
fruits.pop()                 # Elemen terakhir
fruits.pop(0)                # Berdasarkan index

# Operasi lain
fruits.sort()                # Urutkan
fruits.reverse()             # Balik urutan
fruits.index("apple")        # Cari index
fruits.count("apple")        # Hitung kemunculan
```

---

## 2. Tuple

### Definisi / Definition

Tuple adalah koleksi data yang **ordered** (terurut), **immutable** (tidak dapat diubah), dan **mengizinkan duplikat**.

```python
# Membuat tuple
coordinates = (10, 20)
rgb_color = (255, 128, 0)
single_element = (42,)  # Perlu koma untuk single element
```

### ✅ Best Practices

| Situasi                    | Gunakan Tuple Ketika...                    |
| -------------------------- | ------------------------------------------ |
| **Data Konstan**           | Nilai tidak boleh diubah setelah dibuat    |
| **Dictionary Keys**        | Butuh koleksi sebagai key dictionary       |
| **Return Multiple Values** | Fungsi mengembalikan lebih dari satu nilai |
| **Unpacking**              | Butuh assign banyak variabel sekaligus     |

### 🎯 Use Cases

```python
# 1. Koordinat/Posisi - tidak boleh berubah
point = (10, 20)
location = (latitude, longitude)

# 2. RGB Color - nilai tetap
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 3. Return multiple values
def get_user_info():
    return ("Alice", 25, "alice@email.com")

name, age, email = get_user_info()  # Unpacking

# 4. Dictionary key (list tidak bisa!)
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
}

# 5. Named Tuple untuk data yang lebih deskriptif
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
```

### ⚠️ Kapan TIDAK Menggunakan Tuple

```python
# ❌ JANGAN: Ketika data perlu dimodifikasi
scores = (90, 85, 88)
scores[0] = 95  # TypeError!

# ✅ Gunakan list jika perlu modifikasi
scores = [90, 85, 88]
scores[0] = 95  # OK
```

### 📌 Methods Penting

```python
numbers = (1, 2, 3, 2, 2, 4)

# Hanya 2 method karena immutable
numbers.count(2)   # 3 (jumlah angka 2)
numbers.index(3)   # 2 (index angka 3)

# Tuple unpacking
a, b, c = (1, 2, 3)
first, *rest = (1, 2, 3, 4, 5)  # first=1, rest=[2,3,4,5]
```

---

## 3. Set

### Definisi / Definition

Set adalah koleksi data yang **unordered** (tidak terurut), **mutable**, dan **tidak mengizinkan duplikat**.

```python
# Membuat set
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Bukan {} (itu dictionary kosong!)
```

### ✅ Best Practices

| Situasi                   | Gunakan Set Ketika...                  |
| ------------------------- | -------------------------------------- |
| **Menghapus Duplikat**    | Perlu koleksi dengan nilai unik        |
| **Cek Keanggotaan Cepat** | Sering mengecek apakah item ada (O(1)) |
| **Operasi Matematika**    | Butuh union, intersection, difference  |
| **Data Tidak Perlu Urut** | Urutan tidak penting                   |

### 🎯 Use Cases

```python
# 1. Menghapus duplikat
names_with_dupes = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = set(names_with_dupes)  # {"Alice", "Bob", "Charlie"}

# 2. Cek keanggotaan cepat - O(1)
allowed_users = {"admin", "moderator", "user"}
if "admin" in allowed_users:
    print("Access granted")

# 3. Operasi matematika set
frontend_devs = {"Alice", "Bob", "Charlie"}
backend_devs = {"Bob", "Diana", "Eve"}

# Fullstack (keduanya)
fullstack = frontend_devs & backend_devs  # {"Bob"}

# Semua developer
all_devs = frontend_devs | backend_devs  # {"Alice", "Bob", "Charlie", "Diana", "Eve"}

# Hanya frontend
only_frontend = frontend_devs - backend_devs  # {"Alice", "Charlie"}

# 4. Validasi input yang diizinkan
VALID_STATUS = {"active", "inactive", "pending"}
user_status = "active"
if user_status in VALID_STATUS:
    print("Valid status")

# 5. Mencari item yang sama/berbeda
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)  # {4, 5}
```

### ⚠️ Kapan TIDAK Menggunakan Set

```python
# ❌ JANGAN: Ketika urutan penting
first_three = {1, 2, 3}
print(first_three)  # Mungkin {2, 3, 1} - urutan tidak dijamin!

# ❌ JANGAN: Ketika butuh duplikat
scores = {100, 85, 100}  # Menjadi {100, 85} - duplikat hilang!

# ❌ JANGAN: Untuk menyimpan data mutable
my_set = {[1, 2, 3]}  # TypeError! List tidak bisa jadi elemen set
```

### 📌 Methods Penting

```python
fruits = {"apple", "banana"}

# Menambah elemen
fruits.add("cherry")           # Satu elemen
fruits.update(["grape", "mango"])  # Multiple elemen

# Menghapus elemen
fruits.remove("banana")        # Error jika tidak ada
fruits.discard("banana")       # Tidak error jika tidak ada
fruits.pop()                   # Hapus elemen random

# Operasi set
set1 = {1, 2, 3}
set2 = {2, 3, 4}

set1 | set2   # Union: {1, 2, 3, 4}
set1 & set2   # Intersection: {2, 3}
set1 - set2   # Difference: {1}
set1 ^ set2   # Symmetric Difference: {1, 4}

# Cek subset/superset
{1, 2}.issubset({1, 2, 3})     # True
{1, 2, 3}.issuperset({1, 2})   # True
```

---

## 4. Dictionary

### Definisi / Definition

Dictionary adalah koleksi data **key-value pairs** yang **ordered** (Python 3.7+), **mutable**, dan **keys harus unik**.

```python
# Membuat dictionary
user = {"name": "Alice", "age": 25}
scores = dict(math=90, english=85)
empty_dict = {}
```

### ✅ Best Practices

| Situasi               | Gunakan Dictionary Ketika...                |
| --------------------- | ------------------------------------------- |
| **Key-Value Mapping** | Data memiliki hubungan key-value yang jelas |
| **Lookup Cepat**      | Butuh akses data O(1) berdasarkan key       |
| **Data Terstruktur**  | Menyimpan objek dengan berbagai atribut     |
| **Counting**          | Menghitung frekuensi kemunculan             |

### 🎯 Use Cases

```python
# 1. User Profile / Object dengan atribut
user = {
    "id": 1,
    "name": "Alice",
    "email": "alice@email.com",
    "is_active": True
}

# 2. Configuration / Settings
config = {
    "debug": True,
    "database": "postgresql",
    "port": 5432
}

# 3. Counting / Frequency
from collections import Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)  # {"apple": 3, "banana": 2, "cherry": 1}

# 4. Caching / Memoization
cache = {}
def expensive_function(n):
    if n in cache:
        return cache[n]
    result = n ** 2  # Operasi mahal
    cache[n] = result
    return result

# 5. Grouping data
students_by_grade = {
    "A": ["Alice", "Bob"],
    "B": ["Charlie", "Diana"],
    "C": ["Eve"]
}

# 6. JSON-like data structure
api_response = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }
}

# 7. Switch-case alternative
def get_day_type(day):
    day_types = {
        "Monday": "weekday",
        "Tuesday": "weekday",
        "Saturday": "weekend",
        "Sunday": "weekend"
    }
    return day_types.get(day, "unknown")
```

### ⚠️ Kapan TIDAK Menggunakan Dictionary

```python
# ❌ JANGAN: Untuk data sederhana berurutan
# Dictionary overkill untuk ini:
items = {"0": "apple", "1": "banana", "2": "cherry"}

# ✅ Gunakan list
items = ["apple", "banana", "cherry"]

# ❌ JANGAN: Ketika key tidak unik
# Duplikat akan tertimpa
scores = {"Alice": 90, "Alice": 95}  # {"Alice": 95}
```

### 📌 Methods Penting

```python
user = {"name": "Alice", "age": 25}

# Akses nilai
user["name"]              # "Alice" (error jika key tidak ada)
user.get("name")          # "Alice" (None jika key tidak ada)
user.get("city", "N/A")   # "N/A" (default value)

# Menambah/Update
user["email"] = "alice@email.com"  # Tambah baru
user.update({"age": 26, "city": "Jakarta"})  # Update multiple

# Menghapus
del user["age"]           # Hapus key
user.pop("email")         # Hapus dan return value
user.popitem()            # Hapus dan return item terakhir

# Iterasi
user.keys()               # dict_keys(['name', 'city'])
user.values()             # dict_values(['Alice', 'Jakarta'])
user.items()              # dict_items([('name', 'Alice'), ...])

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1}
dict2 = {"b": 2}
merged = dict1 | dict2    # {"a": 1, "b": 2}
```

---

## Perbandingan / Comparison

### 🔍 Performa (Big O)

| Operasi             | List   | Tuple | Set  | Dict |
| ------------------- | ------ | ----- | ---- | ---- |
| **Access by Index** | O(1)   | O(1)  | ❌   | ❌   |
| **Access by Key**   | ❌     | ❌    | ❌   | O(1) |
| **Search (in)**     | O(n)   | O(n)  | O(1) | O(1) |
| **Insert**          | O(1)\* | ❌    | O(1) | O(1) |
| **Delete**          | O(n)   | ❌    | O(1) | O(1) |

\*O(1) untuk append, O(n) untuk insert di tengah

### 💾 Penggunaan Memory

```python
import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

print(f"List:  {sys.getsizeof(my_list)} bytes")   # ~96 bytes
print(f"Tuple: {sys.getsizeof(my_tuple)} bytes")  # ~80 bytes (lebih kecil!)
print(f"Set:   {sys.getsizeof(my_set)} bytes")    # ~216 bytes
print(f"Dict:  {sys.getsizeof(my_dict)} bytes")   # ~232 bytes
```

> 💡 **Tip**: Tuple menggunakan memory paling sedikit karena immutable.

---

## Kapan Menggunakan? / When to Use?

### 🎯 Quick Decision Guide

```
Butuh key-value pairs?
├── Ya → Dictionary
└── Tidak ─┐
           │
           Butuh nilai unik saja?
           ├── Ya → Set
           └── Tidak ─┐
                      │
                      Data boleh diubah?
                      ├── Ya → List
                      └── Tidak → Tuple
```

### 📊 Rangkuman Penggunaan

| Gunakan...     | Ketika...                            | Contoh                        |
| -------------- | ------------------------------------ | ----------------------------- |
| **List**       | Koleksi dinamis, urut, bisa duplikat | Shopping cart, history, queue |
| **Tuple**      | Data konstan, return multiple values | Koordinat, RGB, config values |
| **Set**        | Nilai unik, cek keanggotaan cepat    | Tags, permissions, dedupe     |
| **Dictionary** | Mapping key-value, lookup cepat      | User profile, config, cache   |

---

## 📂 Struktur Folder

```
data_structure/
├── README.md          # Dokumentasi ini
├── list/              # Contoh dan latihan List
├── tuple/             # Contoh dan latihan Tuple
├── sets/              # Contoh dan latihan Set
└── dictionary/        # Contoh dan latihan Dictionary
```

---

## 📚 Referensi Tambahan

- [Python Official Documentation - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python - Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Real Python - Sets](https://realpython.com/python-sets/)
- [Real Python - Dictionaries](https://realpython.com/python-dicts/)

---

_Dokumentasi ini dibuat untuk membantu memahami kapan dan bagaimana menggunakan struktur data Python yang tepat._
