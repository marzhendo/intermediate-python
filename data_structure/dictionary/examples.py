"""
Python Dictionary - Contoh Penggunaan
======================================
File ini berisi contoh-contoh praktis penggunaan Dictionary di Python.
"""

# =============================================================================
# 1. MEMBUAT DICTIONARY
# =============================================================================

print("=== 1. MEMBUAT DICTIONARY ===")

# Dictionary kosong
empty_dict = {}
empty_dict2 = dict()

# Dictionary dengan elemen
user = {"name": "Alice", "age": 25, "city": "Jakarta"}
scores = dict(math=90, english=85, science=88)

# Dari list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
from_pairs = dict(pairs)

print(f"user: {user}")
print(f"scores: {scores}")
print(f"from_pairs: {from_pairs}")
print()

# =============================================================================
# 2. MENGAKSES NILAI
# =============================================================================

print("=== 2. MENGAKSES NILAI ===")

user = {"name": "Alice", "age": 25, "city": "Jakarta"}

# Direct access
print(f"user['name']: {user['name']}")

# get() - aman, tidak error
print(f"user.get('name'): {user.get('name')}")
print(f"user.get('country'): {user.get('country')}")  # None
print(f"user.get('country', 'Unknown'): {user.get('country', 'Unknown')}")

# keys(), values(), items()
print(f"keys: {list(user.keys())}")
print(f"values: {list(user.values())}")
print(f"items: {list(user.items())}")
print()

# =============================================================================
# 3. MODIFIKASI DICTIONARY
# =============================================================================

print("=== 3. MODIFIKASI DICTIONARY ===")

user = {"name": "Alice"}
print(f"Awal: {user}")

# Tambah/Update
user["age"] = 25
print(f"Setelah tambah age: {user}")

user.update({"city": "Jakarta", "email": "alice@email.com"})
print(f"Setelah update: {user}")

# setdefault - set jika belum ada
user.setdefault("status", "active")
print(f"Setelah setdefault status: {user}")

user.setdefault("status", "inactive")  # Tidak berubah karena sudah ada
print(f"Setelah setdefault lagi: {user}")

# Hapus
del user["email"]
print(f"Setelah del email: {user}")

age = user.pop("age")
print(f"Setelah pop age (value: {age}): {user}")
print()

# =============================================================================
# 4. DICTIONARY COMPREHENSION
# =============================================================================

print("=== 4. DICTIONARY COMPREHENSION ===")

# Basic
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Dengan kondisi
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Dari dua list
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_age = {name: age for name, age in zip(names, ages)}
print(f"Name-age mapping: {name_age}")

# Invert dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Inverted: {inverted}")

# Filter dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
passed = {name: score for name, score in scores.items() if score >= 80}
print(f"Passed (>=80): {passed}")
print()

# =============================================================================
# 5. NESTED DICTIONARY
# =============================================================================

print("=== 5. NESTED DICTIONARY ===")

# Struktur nested
company = {
    "name": "Tech Corp",
    "departments": {
        "engineering": {
            "head": "Alice",
            "employees": ["Bob", "Charlie", "Diana"],
            "budget": 1000000
        },
        "marketing": {
            "head": "Eve",
            "employees": ["Frank", "Grace"],
            "budget": 500000
        }
    }
}

# Akses nested
print(f"Company: {company['name']}")
print(f"Engineering head: {company['departments']['engineering']['head']}")
print(f"Marketing budget: Rp{company['departments']['marketing']['budget']:,}")

# Safe nested access
def get_nested(data, *keys, default=None):
    for key in keys:
        try:
            data = data[key]
        except (KeyError, TypeError):
            return default
    return data

# Penggunaan
budget = get_nested(company, "departments", "hr", "budget", default=0)
print(f"HR budget (not exists): Rp{budget}")
print()

# =============================================================================
# 6. DEFAULTDICT
# =============================================================================

print("=== 6. DEFAULTDICT ===")

from collections import defaultdict

# Dengan list sebagai default - untuk grouping
print("Grouping dengan defaultdict(list):")
students_by_grade = defaultdict(list)
students = [
    ("Alice", "A"), ("Bob", "B"), ("Charlie", "A"),
    ("Diana", "B"), ("Eve", "A"), ("Frank", "C")
]
for name, grade in students:
    students_by_grade[grade].append(name)

for grade, names in sorted(students_by_grade.items()):
    print(f"  Grade {grade}: {names}")

# Dengan int sebagai default - untuk counting
print("\nCounting dengan defaultdict(int):")
word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    word_count[word] += 1

for word, count in word_count.items():
    print(f"  {word}: {count}")

# Dengan set sebagai default - untuk unique collection
print("\nUnique values dengan defaultdict(set):")
user_actions = defaultdict(set)
logs = [
    ("Alice", "login"), ("Bob", "view"),
    ("Alice", "click"), ("Alice", "login"),  # Duplikat
    ("Bob", "click"), ("Bob", "view"),       # Duplikat
]
for user, action in logs:
    user_actions[user].add(action)

for user, actions in user_actions.items():
    print(f"  {user}: {actions}")
print()

# =============================================================================
# 7. COUNTER
# =============================================================================

print("=== 7. COUNTER ===")

from collections import Counter

# Counting dari list
words = ["apple", "banana", "apple", "cherry", "banana", "apple", "apple"]
word_count = Counter(words)
print(f"Word count: {word_count}")

# Counting dari string
char_count = Counter("mississippi")
print(f"Char count: {char_count}")

# most_common
print(f"Most common 2: {word_count.most_common(2)}")

# Operasi aritmatika
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"c1 + c2: {c1 + c2}")
print(f"c1 - c2: {c1 - c2}")

# Elements
print(f"elements of Counter(a=2, b=1): {list(Counter(a=2, b=1).elements())}")
print()

# =============================================================================
# 8. USE CASE: CACHING / MEMOIZATION
# =============================================================================

print("=== 8. USE CASE: CACHING / MEMOIZATION ===")

# Manual cache
cache = {}
call_count = 0

def fibonacci(n):
    global call_count
    call_count += 1
    
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    
    result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

result = fibonacci(30)
print(f"fibonacci(30) = {result}")
print(f"Total function calls: {call_count}")

# Dengan functools.lru_cache (built-in)
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

result = fibonacci_cached(30)
print(f"fibonacci_cached(30) = {result}")
print(f"Cache info: {fibonacci_cached.cache_info()}")
print()

# =============================================================================
# 9. USE CASE: CONFIGURATION
# =============================================================================

print("=== 9. USE CASE: CONFIGURATION ===")

# Default config
DEFAULT_CONFIG = {
    "debug": False,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "cache": {
        "enabled": True,
        "ttl": 3600
    },
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(message)s"
    }
}

# User/Environment config override
user_config = {
    "debug": True,
    "database": {
        "host": "production.db.com",
        "port": 5432,
        "name": "production"
    }
}

def deep_merge(base, override):
    """Deep merge two dictionaries"""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

# Merge configs
final_config = deep_merge(DEFAULT_CONFIG, user_config)

print("Final Configuration:")
import json
print(json.dumps(final_config, indent=2))
print()

# =============================================================================
# 10. USE CASE: DISPATCH TABLE (SWITCH-CASE)
# =============================================================================

print("=== 10. USE CASE: DISPATCH TABLE (SWITCH-CASE) ===")

def handle_get(request):
    return f"GET: Fetching data for {request.get('path')}"

def handle_post(request):
    return f"POST: Creating resource at {request.get('path')}"

def handle_put(request):
    return f"PUT: Updating resource at {request.get('path')}"

def handle_delete(request):
    return f"DELETE: Removing resource at {request.get('path')}"

def handle_unknown(request):
    return f"Unknown method: {request.get('method')}"

# Dispatch table
handlers = {
    "GET": handle_get,
    "POST": handle_post,
    "PUT": handle_put,
    "DELETE": handle_delete
}

# Simulasi HTTP requests
requests = [
    {"method": "GET", "path": "/users"},
    {"method": "POST", "path": "/users"},
    {"method": "PUT", "path": "/users/1"},
    {"method": "DELETE", "path": "/users/1"},
    {"method": "PATCH", "path": "/users/1"},
]

for req in requests:
    handler = handlers.get(req["method"], handle_unknown)
    result = handler(req)
    print(f"  {result}")
print()

# =============================================================================
# 11. USE CASE: GROUPING DATA
# =============================================================================

print("=== 11. USE CASE: GROUPING DATA ===")

from collections import defaultdict

# Data transaksi
transactions = [
    {"date": "2024-01-01", "category": "food", "amount": 50000},
    {"date": "2024-01-01", "category": "transport", "amount": 25000},
    {"date": "2024-01-02", "category": "food", "amount": 75000},
    {"date": "2024-01-02", "category": "entertainment", "amount": 100000},
    {"date": "2024-01-03", "category": "food", "amount": 60000},
    {"date": "2024-01-03", "category": "transport", "amount": 30000},
]

# Group by category
by_category = defaultdict(list)
for tx in transactions:
    by_category[tx["category"]].append(tx)

print("Transactions by category:")
for category, txs in by_category.items():
    total = sum(tx["amount"] for tx in txs)
    print(f"  {category}: {len(txs)} transactions, total Rp{total:,}")

# Group by date
by_date = defaultdict(list)
for tx in transactions:
    by_date[tx["date"]].append(tx)

print("\nDaily totals:")
for date, txs in sorted(by_date.items()):
    total = sum(tx["amount"] for tx in txs)
    print(f"  {date}: Rp{total:,}")
print()

# =============================================================================
# 12. USE CASE: JSON DATA HANDLING
# =============================================================================

print("=== 12. USE CASE: JSON DATA HANDLING ===")

import json

# Parse JSON
json_string = '''
{
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "active": true},
            {"id": 2, "name": "Bob", "active": false}
        ],
        "total": 2
    }
}
'''

data = json.loads(json_string)
print(f"Status: {data['status']}")
print(f"Total users: {data['data']['total']}")
print("Active users:")
for user in data["data"]["users"]:
    if user["active"]:
        print(f"  - {user['name']}")

# Convert ke JSON
response = {
    "message": "User created",
    "user": {"id": 3, "name": "Charlie"}
}
json_output = json.dumps(response, indent=2)
print(f"\nJSON output:\n{json_output}")
print()

# =============================================================================
# 13. USE CASE: INVENTORY SYSTEM
# =============================================================================

print("=== 13. USE CASE: INVENTORY SYSTEM ===")

class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "price": price}
        print(f"Added {quantity} {name}(s)")
    
    def remove_item(self, name, quantity):
        if name not in self.items:
            print(f"Item '{name}' not found")
            return
        
        if self.items[name]["quantity"] < quantity:
            print(f"Not enough {name} in stock")
            return
        
        self.items[name]["quantity"] -= quantity
        if self.items[name]["quantity"] == 0:
            del self.items[name]
        print(f"Removed {quantity} {name}(s)")
    
    def get_stock(self, name):
        return self.items.get(name, {}).get("quantity", 0)
    
    def get_total_value(self):
        return sum(item["quantity"] * item["price"] for item in self.items.values())
    
    def show_inventory(self):
        print("\n--- Inventory ---")
        for name, info in self.items.items():
            value = info["quantity"] * info["price"]
            print(f"  {name}: {info['quantity']} x Rp{info['price']:,} = Rp{value:,}")
        print(f"Total value: Rp{self.get_total_value():,}")
        print("-----------------\n")

# Penggunaan
inventory = Inventory()
inventory.add_item("Laptop", 5, 15000000)
inventory.add_item("Mouse", 20, 250000)
inventory.add_item("Keyboard", 15, 500000)
inventory.show_inventory()

inventory.remove_item("Mouse", 5)
inventory.add_item("Laptop", 3)
inventory.show_inventory()

print("=== SELESAI ===")
