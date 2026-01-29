# 📝 Python List

## Definisi

List adalah struktur data yang **ordered**, **mutable**, dan **mengizinkan duplikat**.

```python
my_list = [1, 2, 3, "hello", True]
```

---

## 🎯 Best Practices & Use Cases

### ✅ Kapan Menggunakan List

| Use Case                  | Contoh                     |
| ------------------------- | -------------------------- |
| **Koleksi Dinamis**       | Shopping cart, to-do list  |
| **Urutan Penting**        | Browser history, undo/redo |
| **Duplikat Dibolehkan**   | Nilai ujian, transaksi     |
| **Stack/Queue Sederhana** | Task queue, call stack     |

### ❌ Kapan TIDAK Menggunakan List

| Situasi                         | Alternatif          |
| ------------------------------- | ------------------- |
| Data tidak boleh berubah        | `tuple`             |
| Cek keanggotaan sering (besar)  | `set`               |
| Key-value mapping               | `dict`              |
| Antrian besar (frequent pop(0)) | `collections.deque` |

---

## 📚 Methods Lengkap

### Menambah Elemen

```python
fruits = ["apple", "banana"]

# append() - tambah di akhir
fruits.append("cherry")
# Result: ["apple", "banana", "cherry"]

# insert() - tambah di posisi tertentu
fruits.insert(0, "mango")
# Result: ["mango", "apple", "banana", "cherry"]

# extend() - gabung dengan list lain
fruits.extend(["grape", "orange"])
# Result: ["mango", "apple", "banana", "cherry", "grape", "orange"]
```

### Menghapus Elemen

```python
fruits = ["apple", "banana", "cherry", "banana"]

# remove() - hapus berdasarkan nilai (pertama ditemukan)
fruits.remove("banana")
# Result: ["apple", "cherry", "banana"]

# pop() - hapus dan return elemen terakhir
last = fruits.pop()
# last = "banana", fruits = ["apple", "cherry"]

# pop(index) - hapus berdasarkan index
first = fruits.pop(0)
# first = "apple", fruits = ["cherry"]

# clear() - hapus semua elemen
fruits.clear()
# Result: []

# del - hapus dengan slicing
numbers = [1, 2, 3, 4, 5]
del numbers[1:3]
# Result: [1, 4, 5]
```

### Mengakses & Mencari

```python
fruits = ["apple", "banana", "cherry", "banana"]

# index() - cari posisi elemen
pos = fruits.index("banana")
# pos = 1 (posisi pertama ditemukan)

# count() - hitung kemunculan
count = fruits.count("banana")
# count = 2

# in operator - cek keanggotaan
exists = "apple" in fruits
# exists = True
```

### Mengurutkan & Membalik

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - urutkan (in-place, mengubah list asli)
numbers.sort()
# Result: [1, 1, 2, 3, 4, 5, 6, 9]

# sort(reverse=True) - urutkan descending
numbers.sort(reverse=True)
# Result: [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - return list baru (tidak mengubah asli)
original = [3, 1, 4]
new_sorted = sorted(original)
# original = [3, 1, 4], new_sorted = [1, 3, 4]

# reverse() - balik urutan (in-place)
numbers = [1, 2, 3]
numbers.reverse()
# Result: [3, 2, 1]

# reversed() - return iterator
numbers = [1, 2, 3]
reversed_list = list(reversed(numbers))
# Result: [3, 2, 1]
```

### Copy

```python
original = [1, 2, [3, 4]]

# copy() - shallow copy
shallow = original.copy()
# atau: shallow = original[:]
# atau: shallow = list(original)

# Shallow copy problem (nested objects masih terhubung)
shallow[2][0] = 999
# original[2][0] juga berubah menjadi 999!

# Deep copy - untuk nested objects
import copy
deep = copy.deepcopy(original)
deep[2][0] = 888
# original[2][0] tetap 999
```

---

## 🔧 Teknik Lanjutan

### List Comprehension

```python
# Basic
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dengan kondisi
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Dengan if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ["even", "odd", "even", "odd", "even"]
```

### Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [start:end:step]
numbers[2:5]      # [2, 3, 4]
numbers[:3]       # [0, 1, 2]
numbers[7:]       # [7, 8, 9]
numbers[::2]      # [0, 2, 4, 6, 8] (every 2nd)
numbers[::-1]     # [9, 8, 7, ..., 0] (reversed)
numbers[1:7:2]    # [1, 3, 5]

# Negative indexing
numbers[-1]       # 9 (last element)
numbers[-3:]      # [7, 8, 9] (last 3)
numbers[:-2]      # [0, 1, 2, 3, 4, 5, 6, 7]
```

### Unpacking

```python
# Basic unpacking
first, second, third = [1, 2, 3]

# Extended unpacking
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

# Swap values
a, b = [1, 2]
a, b = b, a
# a = 2, b = 1
```

---

## 📊 Kompleksitas Waktu (Big O)

| Operasi        | Kompleksitas | Catatan            |
| -------------- | ------------ | ------------------ |
| `append()`     | O(1)         | Amortized          |
| `pop()`        | O(1)         | Dari akhir         |
| `pop(0)`       | O(n)         | Perlu geser elemen |
| `insert(0, x)` | O(n)         | Perlu geser elemen |
| `x in list`    | O(n)         | Linear search      |
| `list[i]`      | O(1)         | Direct access      |
| `sort()`       | O(n log n)   | Timsort            |
| `len()`        | O(1)         | Cached             |

---

## 💡 Tips & Tricks

```python
# 1. Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5, 6]

# 2. Remove duplicates while maintaining order
items = [1, 2, 2, 3, 1, 4]
unique = list(dict.fromkeys(items))
# [1, 2, 3, 4]

# 3. Zip multiple lists
names = ["Alice", "Bob"]
ages = [25, 30]
combined = list(zip(names, ages))
# [("Alice", 25), ("Bob", 30)]

# 4. Enumerate for index + value
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 5. Filter dengan kondisi
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]

# 6. Map untuk transformasi
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10]
```

---

## 📁 File dalam Folder Ini

```
list/
├── README.md           # Dokumentasi ini
├── examples.py         # Contoh penggunaan
└── exercises.py        # Latihan
```
