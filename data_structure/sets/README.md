# 🔵 Python Set

## Definisi

Set adalah struktur data yang **unordered**, **mutable**, dan **tidak mengizinkan duplikat**.

```python
my_set = {1, 2, 3, 4, 5}
empty_set = set()  # Bukan {} - itu dict kosong!
```

---

## 🎯 Best Practices & Use Cases

### ✅ Kapan Menggunakan Set

| Use Case                   | Contoh                          |
| -------------------------- | ------------------------------- |
| **Menghapus Duplikat**     | Unique values dari list         |
| **Cek Keanggotaan Cepat**  | `if item in allowed_items`      |
| **Operasi Matematika Set** | Union, intersection, difference |
| **Data Tidak Perlu Urut**  | Tags, categories, permissions   |

### ❌ Kapan TIDAK Menggunakan Set

| Situasi                     | Alternatif  |
| --------------------------- | ----------- |
| Urutan penting              | `list`      |
| Butuh duplikat              | `list`      |
| Key-value mapping           | `dict`      |
| Elemen mutable (list, dict) | Tidak bisa! |

---

## 📚 Methods Lengkap

### Menambah Elemen

```python
fruits = {"apple", "banana"}

# add() - tambah satu elemen
fruits.add("cherry")
# {"apple", "banana", "cherry"}

# update() - tambah multiple elemen
fruits.update(["grape", "mango"])
# {"apple", "banana", "cherry", "grape", "mango"}

# update dengan set lain
fruits.update({"orange", "kiwi"})
```

### Menghapus Elemen

```python
fruits = {"apple", "banana", "cherry", "grape"}

# remove() - hapus elemen (ERROR jika tidak ada)
fruits.remove("banana")
# KeyError jika elemen tidak ada!

# discard() - hapus elemen (TIDAK error jika tidak ada)
fruits.discard("mango")  # Aman, tidak error

# pop() - hapus dan return elemen random
random_fruit = fruits.pop()

# clear() - hapus semua
fruits.clear()
# set()
```

---

## 🔢 Operasi Matematika Set

### Visual Representation

```
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}

Union (A | B):        {1, 2, 3, 4, 5, 6}  ← Semua elemen
Intersection (A & B): {3, 4}              ← Elemen yang sama
Difference (A - B):   {1, 2}              ← Di A tapi tidak di B
Symmetric (A ^ B):    {1, 2, 5, 6}        ← Di salah satu, tapi tidak keduanya
```

### Implementasi

```python
frontend = {"Alice", "Bob", "Charlie", "Diana"}
backend = {"Charlie", "Diana", "Eve", "Frank"}

# UNION - semua elemen dari kedua set
all_devs = frontend | backend
# atau: frontend.union(backend)
# {"Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"}

# INTERSECTION - elemen yang ada di keduanya
fullstack = frontend & backend
# atau: frontend.intersection(backend)
# {"Charlie", "Diana"}

# DIFFERENCE - di set pertama tapi tidak di kedua
only_frontend = frontend - backend
# atau: frontend.difference(backend)
# {"Alice", "Bob"}

only_backend = backend - frontend
# {"Eve", "Frank"}

# SYMMETRIC DIFFERENCE - di salah satu, tapi tidak keduanya
specialists = frontend ^ backend
# atau: frontend.symmetric_difference(backend)
# {"Alice", "Bob", "Eve", "Frank"}
```

### In-Place Operations

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# update() - union in-place
set1.update(set2)
# set1 = {1, 2, 3, 4, 5}

# intersection_update() - intersection in-place
set1 = {1, 2, 3}
set1.intersection_update(set2)
# set1 = {3}

# difference_update() - difference in-place
set1 = {1, 2, 3}
set1.difference_update(set2)
# set1 = {1, 2}

# symmetric_difference_update()
set1 = {1, 2, 3}
set1.symmetric_difference_update(set2)
# set1 = {1, 2, 4, 5}
```

---

## 🔍 Operasi Perbandingan

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}

# issubset() - Apakah A subset dari B?
set1.issubset(set2)        # True (semua elemen set1 ada di set2)
set1 <= set2               # True (operator alternatif)
set1 < set2                # True (proper subset - subset tapi tidak sama)

# issuperset() - Apakah A superset dari B?
set2.issuperset(set1)      # True
set2 >= set1               # True (operator alternatif)
set2 > set1                # True (proper superset)

# isdisjoint() - Tidak ada elemen yang sama?
{1, 2}.isdisjoint({3, 4})  # True (tidak ada yang sama)
{1, 2}.isdisjoint({2, 3})  # False (ada 2 yang sama)

# Equality
set1 == set3               # True
set1 == set2               # False
```

---

## 🔧 Use Cases Praktis

### 1. Menghapus Duplikat

```python
# Dari list
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
unique_names = list(set(names))
# ["Alice", "Bob", "Charlie"] (urutan mungkin berbeda)

# Mempertahankan urutan (Python 3.7+)
unique_ordered = list(dict.fromkeys(names))
# ["Alice", "Bob", "Charlie"]
```

### 2. Membership Testing (Cepat!)

```python
# ❌ Slow dengan list - O(n)
allowed_users_list = ["admin", "moderator", "user", ...]  # 10000 items
if "admin" in allowed_users_list:  # O(n) = slow
    pass

# ✅ Fast dengan set - O(1)
allowed_users_set = {"admin", "moderator", "user", ...}
if "admin" in allowed_users_set:  # O(1) = fast!
    pass
```

### 3. Mencari Kesamaan & Perbedaan

```python
# File comparison
file1_lines = set(open("file1.txt").readlines())
file2_lines = set(open("file2.txt").readlines())

# Lines yang sama
common = file1_lines & file2_lines

# Lines hanya di file1
only_file1 = file1_lines - file2_lines

# Lines hanya di file2
only_file2 = file2_lines - file1_lines
```

### 4. Validasi Input

```python
VALID_STATUSES = {"pending", "approved", "rejected", "processing"}

def update_status(new_status):
    if new_status not in VALID_STATUSES:
        raise ValueError(f"Invalid status. Must be one of: {VALID_STATUSES}")
    # proceed with update
```

### 5. Counting Unique Items

```python
transactions = ["buy", "sell", "buy", "hold", "buy", "sell"]
unique_actions = len(set(transactions))
# 3 unique actions
```

### 6. Finding Common Elements

```python
# Skill matching
job_requirements = {"Python", "SQL", "Git", "Docker"}
candidate_skills = {"Python", "JavaScript", "Git", "React"}

# Skills yang match
matching = job_requirements & candidate_skills
# {"Python", "Git"}

# Skills yang kurang
missing = job_requirements - candidate_skills
# {"SQL", "Docker"}

# Match percentage
match_percent = len(matching) / len(job_requirements) * 100
# 50%
```

---

## ❄️ Frozen Set

Frozen set adalah **immutable** version dari set.

```python
# Membuat frozen set
frozen = frozenset([1, 2, 3, 4, 5])

# Tidak bisa dimodifikasi
frozen.add(6)     # Error! AttributeError

# Bisa jadi dictionary key
cache = {
    frozenset({1, 2}): "result_a",
    frozenset({3, 4}): "result_b"
}

# Bisa jadi element dari set lain
set_of_sets = {frozenset({1, 2}), frozenset({3, 4})}

# Operasi set tetap bisa
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({3, 4, 5})
fs1 | fs2  # frozenset({1, 2, 3, 4, 5})
fs1 & fs2  # frozenset({3})
```

---

## 💡 Tips & Tricks

```python
# 1. Set comprehension
squares = {x**2 for x in range(10)}
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

evens = {x for x in range(20) if x % 2 == 0}
# {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# 2. Convert string ke set of characters
chars = set("hello")
# {'h', 'e', 'l', 'o'}

# 3. Cek apakah ada elemen yang sama
has_common = bool({1, 2, 3} & {3, 4, 5})  # True

# 4. Remove items from list based on set
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_remove = {2, 4, 6, 8, 10}
filtered = [x for x in items if x not in to_remove]
# [1, 3, 5, 7, 9]

# 5. Multiple membership test
if value in {"option1", "option2", "option3"}:
    pass  # Lebih efisien dari: if value == "option1" or value == "option2" ...

# 6. Unique random sampling
import random
unique_numbers = set()
while len(unique_numbers) < 10:
    unique_numbers.add(random.randint(1, 100))
```

---

## 📊 Kompleksitas Waktu (Big O)

| Operasi          | Average     | Worst   |
| ---------------- | ----------- | ------- |
| `add()`          | O(1)        | O(n)    |
| `remove()`       | O(1)        | O(n)    |
| `x in set`       | O(1)        | O(n)    |
| `union()`        | O(m+n)      | O(m+n)  |
| `intersection()` | O(min(m,n)) | O(m\*n) |
| `difference()`   | O(m)        | O(m)    |

> Worst case jarang terjadi (hanya saat banyak hash collision)

---

## 📁 File dalam Folder Ini

```
sets/
├── README.md           # Dokumentasi ini
├── examples.py         # Contoh penggunaan
└── exercises.py        # Latihan
```
