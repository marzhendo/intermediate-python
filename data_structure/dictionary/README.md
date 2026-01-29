# 📖 Python Dictionary

## Definisi

Dictionary adalah struktur data **key-value pairs** yang **ordered** (Python 3.7+), **mutable**, dan **keys harus unik**.

```python
my_dict = {"name": "Alice", "age": 25, "city": "Jakarta"}
empty_dict = {}
# atau
empty_dict = dict()
```

---

## 🎯 Best Practices & Use Cases

### ✅ Kapan Menggunakan Dictionary

| Use Case                | Contoh                        |
| ----------------------- | ----------------------------- |
| **Key-Value Mapping**   | User profiles, configurations |
| **Lookup Cepat (O(1))** | Cache, index                  |
| **Counting/Frequency**  | Word count, histogram         |
| **Grouping Data**       | Categorization                |
| **JSON-like Data**      | API response, configs         |

### ❌ Kapan TIDAK Menggunakan Dictionary

| Situasi                   | Alternatif                    |
| ------------------------- | ----------------------------- |
| Data berurutan sederhana  | `list` atau `tuple`           |
| Hanya butuh nilai unik    | `set`                         |
| Keys bisa duplikat        | `list` of tuples              |
| Data terstruktur kompleks | `dataclass` atau `namedtuple` |

---

## 📚 Methods Lengkap

### Mengakses Nilai

```python
user = {"name": "Alice", "age": 25, "city": "Jakarta"}

# Direct access - Error jika key tidak ada!
name = user["name"]  # "Alice"
# user["country"]    # KeyError!

# get() - Aman, return None jika tidak ada
country = user.get("country")  # None
country = user.get("country", "Unknown")  # "Unknown" (default)

# keys(), values(), items()
user.keys()    # dict_keys(['name', 'age', 'city'])
user.values()  # dict_values(['Alice', 25, 'Jakarta'])
user.items()   # dict_items([('name', 'Alice'), ('age', 25), ...])
```

### Menambah & Mengupdate

```python
user = {"name": "Alice"}

# Direct assignment
user["age"] = 25
# {"name": "Alice", "age": 25}

# update() - merge dengan dict lain
user.update({"city": "Jakarta", "email": "alice@email.com"})
# {"name": "Alice", "age": 25, "city": "Jakarta", "email": "..."}

# update dengan keyword arguments
user.update(phone="123456", country="Indonesia")

# setdefault() - set jika belum ada, return value
user.setdefault("status", "active")  # Set "active" jika belum ada
# Returns: "active"

# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # {"a": 1, "b": 3, "c": 4}
```

### Menghapus

```python
user = {"name": "Alice", "age": 25, "city": "Jakarta"}

# del - hapus key tertentu
del user["age"]
# {"name": "Alice", "city": "Jakarta"}

# pop() - hapus dan return value
city = user.pop("city")
# city = "Jakarta", user = {"name": "Alice"}

# pop() dengan default (tidak error jika tidak ada)
country = user.pop("country", "Not found")
# country = "Not found"

# popitem() - hapus dan return item terakhir (LIFO)
user = {"name": "Alice", "age": 25}
last_item = user.popitem()
# last_item = ("age", 25), user = {"name": "Alice"}

# clear() - hapus semua
user.clear()
# {}
```

---

## 🔧 Teknik Lanjutan

### Dictionary Comprehension

```python
# Basic
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dengan kondisi
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Dari dua list
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_age = {name: age for name, age in zip(names, ages)}
# {"Alice": 25, "Bob": 30, "Charlie": 35}

# Invert dictionary (swap key-value)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

# Filter dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
passed = {name: score for name, score in scores.items() if score >= 80}
# {"Alice": 85, "Bob": 92, "Diana": 95}
```

### Nested Dictionary

```python
# Struktur nested
users = {
    "user1": {
        "name": "Alice",
        "profile": {
            "age": 25,
            "city": "Jakarta"
        }
    },
    "user2": {
        "name": "Bob",
        "profile": {
            "age": 30,
            "city": "Bandung"
        }
    }
}

# Akses nested
alice_city = users["user1"]["profile"]["city"]  # "Jakarta"

# Safe nested access
def get_nested(data, *keys, default=None):
    for key in keys:
        try:
            data = data[key]
        except (KeyError, TypeError):
            return default
    return data

city = get_nested(users, "user1", "profile", "city")  # "Jakarta"
missing = get_nested(users, "user1", "profile", "country", default="Unknown")
```

### DefaultDict

```python
from collections import defaultdict

# Dengan list sebagai default
grouped = defaultdict(list)
data = [("fruit", "apple"), ("fruit", "banana"), ("veggie", "carrot")]
for category, item in data:
    grouped[category].append(item)
# {"fruit": ["apple", "banana"], "veggie": ["carrot"]}

# Dengan int sebagai default (untuk counting)
word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    word_count[word] += 1
# {"apple": 3, "banana": 2, "cherry": 1}

# Dengan set sebagai default
tags = defaultdict(set)
# Auto-create empty set jika key tidak ada
```

### Counter

```python
from collections import Counter

# Counting dari list
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
# Counter({"apple": 3, "banana": 2, "cherry": 1})

# Counting dari string
char_count = Counter("mississippi")
# Counter({"i": 4, "s": 4, "p": 2, "m": 1})

# Methods berguna
word_count.most_common(2)  # [("apple", 3), ("banana", 2)]
word_count.total()         # 6 (Python 3.10+)

# Operasi aritmatika
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2  # Counter({'a': 4, 'b': 3})
c1 - c2  # Counter({'a': 2})  # negative values diabaikan
```

### OrderedDict

```python
from collections import OrderedDict

# Sebelum Python 3.7, dict tidak menjamin urutan
# OrderedDict menjamin urutan dan punya method tambahan

od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

# Move to end
od.move_to_end("a")
# OrderedDict([("b", 2), ("c", 3), ("a", 1)])

# Move to beginning
od.move_to_end("a", last=False)
# OrderedDict([("a", 1), ("b", 2), ("c", 3)])

# Pop last (LIFO)
od.popitem()  # ("c", 3)

# Pop first (FIFO)
od.popitem(last=False)  # ("a", 1)
```

---

## 🎯 Common Patterns

### 1. Caching / Memoization

```python
cache = {}

def expensive_computation(n):
    if n in cache:
        return cache[n]

    result = n ** 2  # Operasi mahal
    cache[n] = result
    return result

# Atau dengan functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 2. Configuration Management

```python
# Default config
DEFAULT_CONFIG = {
    "debug": False,
    "database": "sqlite",
    "port": 8080,
    "timeout": 30
}

# User config
user_config = {
    "debug": True,
    "port": 3000
}

# Merge (user config overrides defaults)
config = {**DEFAULT_CONFIG, **user_config}
# {"debug": True, "database": "sqlite", "port": 3000, "timeout": 30}
```

### 3. Dispatch Table / Switch-Case

```python
def handle_get():
    return "GET request"

def handle_post():
    return "POST request"

def handle_put():
    return "PUT request"

def handle_default():
    return "Unknown method"

# Dispatch table
handlers = {
    "GET": handle_get,
    "POST": handle_post,
    "PUT": handle_put
}

# Usage
method = "POST"
handler = handlers.get(method, handle_default)
result = handler()  # "POST request"
```

### 4. Grouping Data

```python
from collections import defaultdict

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "B"},
    {"name": "Eve", "grade": "A"}
]

# Group by grade
by_grade = defaultdict(list)
for student in students:
    by_grade[student["grade"]].append(student["name"])

# {"A": ["Alice", "Charlie", "Eve"], "B": ["Bob", "Diana"]}
```

### 5. JSON Data Handling

```python
import json

# Parse JSON string
json_str = '{"name": "Alice", "age": 25}'
data = json.loads(json_str)

# Convert to JSON string
dict_data = {"name": "Bob", "scores": [90, 85, 95]}
json_output = json.dumps(dict_data, indent=2)

# Pretty print
print(json.dumps(data, indent=4, sort_keys=True))
```

### 6. Frequency Count

```python
# Tanpa Counter
text = "hello world hello python"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
# {"hello": 2, "world": 1, "python": 1}

# Dengan Counter
from collections import Counter
freq = Counter(text.split())
# Counter({"hello": 2, "world": 1, "python": 1})
```

---

## 💡 Tips & Tricks

```python
# 1. Iterate dengan keys, values, atau items
for key in my_dict:           # Iterate keys
    pass
for value in my_dict.values(): # Iterate values
    pass
for key, value in my_dict.items():  # Iterate both
    pass

# 2. Check if key exists
if "name" in user:  # ✅ Benar
    pass
if user.get("name"):  # ⚠️ False jika value = None, "", 0

# 3. Safe default untuk nested dict
data = {"a": {"b": {"c": 1}}}
value = data.get("a", {}).get("b", {}).get("c", 0)

# 4. Merge multiple dicts
result = {**dict1, **dict2, **dict3}

# 5. Create dict from keys dengan default value
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
# {"a": 0, "b": 0, "c": 0}

# 6. Unpack dict sebagai function arguments
def greet(name, age, city):
    print(f"{name}, {age}, from {city}")

user = {"name": "Alice", "age": 25, "city": "Jakarta"}
greet(**user)  # Alice, 25, from Jakarta

# 7. Walrus operator dengan dict.get() (Python 3.8+)
if (value := data.get("key")) is not None:
    print(value)
```

---

## 📊 Kompleksitas Waktu (Big O)

| Operasi             | Average | Worst |
| ------------------- | ------- | ----- |
| `dict[key]`         | O(1)    | O(n)  |
| `dict[key] = value` | O(1)    | O(n)  |
| `key in dict`       | O(1)    | O(n)  |
| `del dict[key]`     | O(1)    | O(n)  |
| `dict.get(key)`     | O(1)    | O(n)  |
| Iteration           | O(n)    | O(n)  |

> Worst case sangat jarang (hanya saat banyak hash collision)

---

## 📁 File dalam Folder Ini

```
dictionary/
├── README.md           # Dokumentasi ini
├── examples.py         # Contoh penggunaan
└── exercises.py        # Latihan
```
