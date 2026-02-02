# 🐍 Intermediate Python Learning Repository

Repositori ini berisi materi pembelajaran Python tingkat menengah (intermediate) yang mencakup **struktur data**, **pemrograman fungsional**, dan **file handling**.

---

## 📋 Daftar Isi

1. [Struktur Data (Data Structures)](#-struktur-data-data-structures)
2. [Pemrograman Fungsional (Functional Programming)](#-pemrograman-fungsional-functional-programming)
3. [File Handling (I/O Operations)](#-file-handling-io-operations)
4. [Struktur Folder](#-struktur-folder)

---

## 📦 Struktur Data (Data Structures)

Mempelajari 4 struktur data bawaan Python beserta kapan dan bagaimana menggunakannya.

| Struktur Data  | Mutable  | Ordered  | Duplicates | Syntax      |
| -------------- | -------- | -------- | ---------- | ----------- |
| **List**       | ✅ Ya    | ✅ Ya    | ✅ Ya      | `[1, 2, 3]` |
| **Tuple**      | ❌ Tidak | ✅ Ya    | ✅ Ya      | `(1, 2, 3)` |
| **Set**        | ✅ Ya    | ❌ Tidak | ❌ Tidak   | `{1, 2, 3}` |
| **Dictionary** | ✅ Ya    | ✅ Ya*   | Keys: ❌   | `{"a": 1}`  |

> *Dictionary ordered sejak Python 3.7+

### 📁 Folder: `data_structure/`

| Sub-folder   | Konsep Utama                                                                 |
|--------------|------------------------------------------------------------------------------|
| `list/`      | Koleksi dinamis, ordered, mutable, methods (append, pop, sort, slice)        |
| `tuple/`     | Data immutable, hashable (bisa jadi dict key), unpacking, memory efficient   |
| `sets/`      | Nilai unik, operasi matematika set (union, intersection, difference)         |
| `dictionary/`| Key-value pairs, lookup cepat O(1), nested dict, dictionary comprehension    |

---

## ⚡ Pemrograman Fungsional (Functional Programming)

Mempelajari paradigma pemrograman fungsional di Python.

### 📁 Folder: `functional_programming/`

#### 🔹 Konsep yang Dipelajari:

| File | Konsep | Deskripsi |
|------|--------|-----------|
| `example.py` | **Pure vs Impure Function** | Fungsi pure tidak memiliki side effect dan selalu mengembalikan output yang sama untuk input yang sama |
| `l_comprehension.py` | **List Comprehension** | Cara ringkas membuat list baru dengan sintaks `[expr for item in iterable if condition]` |
| `decorator.py` | **Decorator** | Fungsi yang membungkus fungsi lain untuk menambah fungsionalitas tanpa mengubah kode asli |
| `measure_t.py` | **Decorator (Praktis)** | Contoh decorator untuk mengukur waktu eksekusi fungsi |
| `generator.py` | **Generator Expression** | Mirip list comprehension tapi lebih hemat memori `(expr for item in iterable)` |
| `gen_func.py` | **Generator Function** | Fungsi dengan `yield` untuk menghasilkan nilai secara lazy (satu per satu) |
| `translate.py`, `hola.py`, `penerjemah_pintar.py` | **Closure** | Fungsi yang "mengingat" variabel dari scope pembuatnya |
| `songs.py`, `transaksi_harian.py`, `fantasy_name.py` | **Higher-Order Functions** | `map()`, `filter()`, `reduce()` - fungsi yang menerima/mengembalikan fungsi lain |
| `total_belanja.py` | **functools.reduce()** | Mengakumulasi nilai dalam iterable menjadi satu hasil |

#### 🎯 Contoh Kode Penting:

**1. List Comprehension vs Generator Expression:**
```python
# List Comprehension - langsung di memori
list_comp = [x**2 for x in range(1000)]  

# Generator Expression - lazy evaluation, hemat memori
gen_exp = (x**2 for x in range(1000))
```

**2. Decorator Pattern:**
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Sebelum fungsi")
        result = func(*args, **kwargs)
        print("Sesudah fungsi")
        return result
    return wrapper

@my_decorator
def say_hello(nama):
    return f"Hello {nama}!"
```

**3. Closure:**
```python
def create_translator(language):
    translations = {"spanish": {"hello": "hola"}}
    def translate(word):
        return translations.get(language, {}).get(word, word)
    return translate  # Inner function "mengingat" language

translate_spanish = create_translator("spanish")
print(translate_spanish("hello"))  # Output: hola
```

**4. Higher-Order Functions (map, filter, reduce):**
```python
import functools

data = [100, -50, 200, 50]

# Filter: hanya nilai positif
positif = list(filter(lambda x: x > 0, data))

# Map: tambah pajak 10%
dengan_pajak = list(map(lambda x: x * 1.1, positif))

# Reduce: jumlahkan semua
total = functools.reduce(lambda a, b: a + b, dengan_pajak)
```

---

## 📂 File Handling (I/O Operations)

Mempelajari cara membaca, menulis, dan memanipulasi file di Python.

### 📁 Folder: `file-i/o/file_handling/`

#### 🔹 Konsep yang Dipelajari:

| File | Konsep | Deskripsi |
|------|--------|-----------|
| `dear_diary.py` | **Basic Write** | Menulis file dengan `open("file.txt", "w")` |
| `game_log.py` | **Write, Append, Read** | Mode file: `w` (write), `a` (append), `r` (read) |
| `playlist.py` | **Dictionary to File** | Menulis dictionary ke file dengan format terstruktur |
| `bestseller.py`, `best_seller.py` | **CSV Reading** | Membaca file CSV menggunakan modul `csv` |
| `packing.py` | **CSV Read/Write + Error Handling** | `csv.reader`, `csv.writer`, dan `try-except-finally` |
| `buku_harianku.py` | **File Operations** | Praktik menulis buku harian ke file |
| `mencatat_tabungan_sederhana.py` | **Practical Exercise** | Aplikasi sederhana pencatatan tabungan |

#### 🎯 Contoh Kode Penting:

**1. Context Manager (with statement):**
```python
# Automatically closes file after block
with open("file.txt", "w") as file:
    file.write("Hello World!")
```

**2. File Modes:**
```python
# Read
with open("file.txt", "r") as f:
    content = f.read()

# Write (overwrite)
with open("file.txt", "w") as f:
    f.write("New content")

# Append
with open("file.txt", "a") as f:
    f.write("\nAppended line")
```

**3. CSV Operations:**
```python
import csv

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing CSV
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
```

---

## 📁 Struktur Folder

```
intermediate-python/
│
├── README.md                    # File ini
│
├── data_structure/              # Struktur Data Python
│   ├── README.md
│   ├── list/
│   │   ├── README.md
│   │   └── examples.py
│   ├── tuple/
│   │   ├── README.md
│   │   └── examples.py
│   ├── sets/
│   │   ├── README.md
│   │   └── examples.py
│   └── dictionary/
│       ├── README.md
│       └── examples.py
│
├── functional_programming/      # Pemrograman Fungsional
│   ├── example.py              # Pure/Impure functions
│   ├── l_comprehension.py      # List comprehension
│   ├── decorator.py            # Decorator basics
│   ├── measure_t.py            # Decorator untuk timing
│   ├── generator.py            # Generator expression
│   ├── gen_func.py             # Generator function (yield)
│   ├── translate.py            # Closure example
│   ├── hola.py                 # Closure translator
│   ├── penerjemah_pintar.py    # Closure advanced
│   ├── songs.py                # map, filter, reduce
│   ├── transaksi_harian.py     # Praktik HOF
│   ├── fantasy_name.py         # Praktik HOF + comprehension
│   └── total_belanja.py        # functools.reduce
│
├── file-i/o/file_handling/      # File Handling
│   ├── dear_diary.py           # Basic write
│   ├── game_log.py             # Write, append, read
│   ├── playlist.py             # Dict to file
│   ├── bestseller.py           # CSV reading
│   ├── packing.py              # CSV + error handling
│   └── ...                     # File latihan lainnya
│
└── *.csv, *.txt                 # File data untuk latihan
```

---

## 🎓 Urutan Belajar yang Disarankan

### Level 1: Data Structures
1. List → dasar koleksi data
2. Tuple → immutability concept
3. Set → unique values & set operations
4. Dictionary → key-value mapping

### Level 2: Functional Programming
1. Pure vs Impure Functions
2. Higher-Order Functions (map, filter, reduce)
3. List Comprehension & Generator Expression
4. Closure
5. Decorator

### Level 3: File Handling
1. Basic read/write operations
2. Context manager (`with` statement)
3. CSV operations
4. Error handling dengan `try-except-finally`

---

## 📚 Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python - Intermediate Topics](https://realpython.com/)
- [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)

---

*Happy Learning! 🚀*
