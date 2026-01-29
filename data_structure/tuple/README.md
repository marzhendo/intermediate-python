# 📦 Python Tuple

## Definisi

Tuple adalah struktur data yang **ordered**, **immutable**, dan **mengizinkan duplikat**.

```python
my_tuple = (1, 2, 3, "hello", True)
single = (42,)  # Single element tuple perlu koma!
```

---

## 🎯 Best Practices & Use Cases

### ✅ Kapan Menggunakan Tuple

| Use Case                   | Contoh                      |
| -------------------------- | --------------------------- |
| **Data Konstan**           | Koordinat, RGB colors       |
| **Dictionary Keys**        | `{(x, y): "value"}`         |
| **Return Multiple Values** | `return (name, age, email)` |
| **Unpacking**              | `x, y, z = (1, 2, 3)`       |
| **Data Heterogen Tetap**   | Record database             |

### ❌ Kapan TIDAK Menggunakan Tuple

| Situasi                     | Alternatif |
| --------------------------- | ---------- |
| Data perlu dimodifikasi     | `list`     |
| Koleksi dinamis             | `list`     |
| Perlu menambah/hapus elemen | `list`     |

---

## 🔑 Mengapa Tuple Immutable?

### Keuntungan Immutability:

```python
# 1. Bisa jadi dictionary key (list tidak bisa!)
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (30, 40): "Point B"
}

# 2. Hashable - bisa masuk ke set
coordinates = {(1, 2), (3, 4), (5, 6)}

# 3. Thread-safe - aman untuk multi-threading
# Tidak ada race condition karena tidak bisa diubah

# 4. Memory lebih efisien
import sys
print(sys.getsizeof([1, 2, 3, 4, 5]))  # ~96 bytes
print(sys.getsizeof((1, 2, 3, 4, 5)))  # ~80 bytes
```

---

## 📚 Methods & Operasi

### Methods Bawaan (Hanya 2!)

```python
numbers = (1, 2, 3, 2, 2, 4, 5)

# count() - hitung kemunculan
count = numbers.count(2)
# count = 3

# index() - cari posisi pertama
pos = numbers.index(4)
# pos = 5
```

### Operasi Tuple

```python
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
# (1, 2, 3, 4, 5, 6)

# Repetition
repeated = (1, 2) * 3
# (1, 2, 1, 2, 1, 2)

# Membership test
exists = 2 in (1, 2, 3)
# True

# Length
length = len((1, 2, 3, 4, 5))
# 5

# Min, Max, Sum
numbers = (5, 2, 8, 1, 9)
print(min(numbers))  # 1
print(max(numbers))  # 9
print(sum(numbers))  # 25
```

---

## 🔧 Teknik Lanjutan

### Tuple Unpacking

```python
# Basic unpacking
x, y, z = (1, 2, 3)

# Dengan nama yang bermakna
name, age, email = ("Alice", 25, "alice@email.com")

# Extended unpacking (Python 3+)
first, *rest = (1, 2, 3, 4, 5)
# first = 1, rest = [2, 3, 4, 5]

first, *middle, last = (1, 2, 3, 4, 5)
# first = 1, middle = [2, 3, 4], last = 5

# Ignore values dengan underscore
name, _, email = ("Alice", 25, "alice@email.com")
# age diabaikan

# Swap tanpa temp variable
a, b = 10, 20
a, b = b, a
# a = 20, b = 10
```

### Named Tuple

```python
from collections import namedtuple

# Definisi named tuple
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age email')

# Membuat instance
p = Point(10, 20)
user = Person("Alice", 25, "alice@email.com")

# Akses dengan nama (lebih readable!)
print(p.x, p.y)           # 10 20
print(user.name)          # Alice
print(user.age)           # 25

# Masih bisa akses dengan index
print(p[0], p[1])         # 10 20

# Convert ke dictionary
print(user._asdict())
# {'name': 'Alice', 'age': 25, 'email': 'alice@email.com'}

# Create dengan nilai baru
new_user = user._replace(age=26)
# Person(name='Alice', age=26, email='alice@email.com')
```

### Tuple sebagai Function Return

```python
# Mengembalikan multiple values
def get_min_max(numbers):
    return (min(numbers), max(numbers))

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Dengan named tuple untuk clarity
from collections import namedtuple

Stats = namedtuple('Stats', ['min', 'max', 'avg', 'count'])

def get_stats(numbers):
    return Stats(
        min=min(numbers),
        max=max(numbers),
        avg=sum(numbers)/len(numbers),
        count=len(numbers)
    )

result = get_stats([1, 2, 3, 4, 5])
print(f"Min: {result.min}, Avg: {result.avg}")  # Min: 1, Avg: 3.0
```

### Tuple Slicing

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing
numbers[2:5]      # (2, 3, 4)
numbers[:3]       # (0, 1, 2)
numbers[7:]       # (7, 8, 9)
numbers[::2]      # (0, 2, 4, 6, 8)
numbers[::-1]     # (9, 8, 7, ..., 0) reversed

# Negative indexing
numbers[-1]       # 9
numbers[-3:]      # (7, 8, 9)
```

---

## 🆚 Tuple vs List

| Aspek           | Tuple        | List          |
| --------------- | ------------ | ------------- |
| **Mutability**  | Immutable ❌ | Mutable ✅    |
| **Syntax**      | `(1, 2, 3)`  | `[1, 2, 3]`   |
| **Memory**      | Lebih kecil  | Lebih besar   |
| **Speed**       | Lebih cepat  | Lebih lambat  |
| **Dict Key**    | ✅ Bisa      | ❌ Tidak bisa |
| **Set Element** | ✅ Bisa      | ❌ Tidak bisa |
| **Methods**     | 2            | Banyak        |
| **Use Case**    | Data tetap   | Data dinamis  |

### Performance Comparison

```python
import timeit

# Tuple creation lebih cepat
tuple_time = timeit.timeit('(1, 2, 3, 4, 5)', number=1000000)
list_time = timeit.timeit('[1, 2, 3, 4, 5]', number=1000000)
print(f"Tuple: {tuple_time:.4f}s")  # ~0.02s
print(f"List: {list_time:.4f}s")    # ~0.06s

# Tuple iteration sedikit lebih cepat
tuple_iter = timeit.timeit('for i in (1,2,3,4,5): pass', number=1000000)
list_iter = timeit.timeit('for i in [1,2,3,4,5]: pass', number=1000000)
```

---

## 💡 Tips & Tricks

```python
# 1. Tuple tanpa parentheses
coordinates = 10, 20, 30  # Valid tuple!
x, y, z = coordinates

# 2. Single element tuple HARUS pakai koma
single = (42,)      # ✅ Tuple
not_tuple = (42)    # ❌ Ini integer!

# 3. Empty tuple
empty = ()
# atau
empty = tuple()

# 4. Convert dari list
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# 5. Nested tuple dengan mutable content
# Hati-hati! Content mutable masih bisa diubah
t = ([1, 2], [3, 4])
t[0].append(999)  # ✅ Legal! t = ([1, 2, 999], [3, 4])
# t[0] = [5, 6]   # ❌ TypeError - tuple immutable

# 6. Zip menghasilkan tuple
names = ["Alice", "Bob"]
ages = [25, 30]
for item in zip(names, ages):
    print(item)  # ('Alice', 25), ('Bob', 30)
```

---

## 📊 Kompleksitas Waktu (Big O)

| Operasi      | Kompleksitas |
| ------------ | ------------ |
| `tuple[i]`   | O(1)         |
| `x in tuple` | O(n)         |
| `len(tuple)` | O(1)         |
| `count()`    | O(n)         |
| `index()`    | O(n)         |
| Iteration    | O(n)         |
| Slicing      | O(k)         |

---

## 📁 File dalam Folder Ini

```
tuple/
├── README.md           # Dokumentasi ini
├── examples.py         # Contoh penggunaan
└── exercises.py        # Latihan
```
