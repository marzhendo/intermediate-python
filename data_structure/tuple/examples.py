"""
Python Tuple - Contoh Penggunaan
=================================
File ini berisi contoh-contoh praktis penggunaan Tuple di Python.
"""

# =============================================================================
# 1. MEMBUAT TUPLE
# =============================================================================

print("=== 1. MEMBUAT TUPLE ===")

# Tuple kosong
empty_tuple = ()
empty_tuple2 = tuple()

# Tuple dengan elemen
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.14, True)

# Single element tuple - HARUS PAKAI KOMA!
single = (42,)
not_tuple = (42)  # Ini integer, bukan tuple!

# Tuple tanpa parentheses
coordinates = 10, 20, 30

print(f"numbers: {numbers}")
print(f"single: {single}, type: {type(single)}")
print(f"not_tuple: {not_tuple}, type: {type(not_tuple)}")
print(f"coordinates: {coordinates}")
print()

# =============================================================================
# 2. MENGAKSES ELEMEN
# =============================================================================

print("=== 2. MENGAKSES ELEMEN ===")

colors = ("red", "green", "blue", "yellow", "purple")

print(f"colors: {colors}")
print(f"Elemen pertama: {colors[0]}")
print(f"Elemen terakhir: {colors[-1]}")
print(f"Slicing [1:4]: {colors[1:4]}")
print(f"Reversed: {colors[::-1]}")
print()

# =============================================================================
# 3. TUPLE IMMUTABILITY
# =============================================================================

print("=== 3. TUPLE IMMUTABILITY ===")

point = (10, 20)
print(f"point: {point}")

# Tidak bisa diubah!
try:
    point[0] = 100
except TypeError as e:
    print(f"Error saat modify tuple: {e}")

# Tapi object mutable di dalam tuple masih bisa diubah!
nested = ([1, 2, 3], [4, 5, 6])
print(f"nested sebelum: {nested}")
nested[0].append(999)  # List di dalam tuple bisa diubah
print(f"nested sesudah: {nested}")
print()

# =============================================================================
# 4. TUPLE UNPACKING
# =============================================================================

print("=== 4. TUPLE UNPACKING ===")

# Basic unpacking
person = ("Alice", 25, "Jakarta")
name, age, city = person
print(f"name: {name}, age: {age}, city: {city}")

# Extended unpacking
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first, second, *middle, last = numbers
print(f"first: {first}, last: {last}")
print(f"middle: {middle}")

# Ignore dengan underscore
data = ("Alice", "secret_password", "alice@email.com")
username, _, email = data
print(f"username: {username}, email: {email}")

# Swap values
a, b = 10, 20
print(f"Sebelum swap: a={a}, b={b}")
a, b = b, a
print(f"Sesudah swap: a={a}, b={b}")
print()

# =============================================================================
# 5. TUPLE SEBAGAI DICTIONARY KEY
# =============================================================================

print("=== 5. TUPLE SEBAGAI DICTIONARY KEY ===")

# List tidak bisa jadi dictionary key (mutable)
try:
    invalid_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"List sebagai key: {e}")

# Tuple bisa jadi dictionary key (immutable)
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (-5, 15): "Point B",
    (10, 20): "Point A Updated"  # Key sama, value di-update
}

print(f"Location at (0, 0): {locations[(0, 0)]}")
print(f"Location at (10, 20): {locations[(10, 20)]}")

# Use case: Memoization dengan tuple key
cache = {}
def get_distance(point1, point2):
    key = (point1, point2)  # Tuple sebagai cache key
    if key in cache:
        print(f"  (from cache)")
        return cache[key]
    
    # Hitung jarak
    import math
    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    cache[key] = distance
    return distance

print(f"Distance: {get_distance((0, 0), (3, 4)):.2f}")
print(f"Distance: {get_distance((0, 0), (3, 4)):.2f}")  # From cache
print()

# =============================================================================
# 6. NAMED TUPLE
# =============================================================================

print("=== 6. NAMED TUPLE ===")

from collections import namedtuple

# Definisi
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age email')
Color = namedtuple('Color', ['red', 'green', 'blue'])

# Membuat instance
p1 = Point(10, 20)
p2 = Point(x=30, y=40)
alice = Person("Alice", 25, "alice@email.com")
red = Color(255, 0, 0)

# Akses dengan nama (lebih readable!)
print(f"Point: x={p1.x}, y={p1.y}")
print(f"Person: {alice.name}, {alice.age} tahun")
print(f"Color: RGB({red.red}, {red.green}, {red.blue})")

# Masih bisa akses dengan index
print(f"Point[0]: {p1[0]}, Point[1]: {p1[1]}")

# Convert ke dictionary
print(f"Person as dict: {alice._asdict()}")

# Create copy dengan nilai baru
alice_new = alice._replace(age=26)
print(f"Updated: {alice_new}")

# Get field names
print(f"Person fields: {Person._fields}")
print()

# =============================================================================
# 7. FUNCTION RETURN MULTIPLE VALUES
# =============================================================================

print("=== 7. FUNCTION RETURN MULTIPLE VALUES ===")

def get_statistics(numbers):
    """Return statistics sebagai tuple"""
    if not numbers:
        return (0, 0, 0, 0)
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    return (min(numbers), max(numbers), average, count)

# Penggunaan dengan unpacking
scores = [85, 92, 78, 95, 88, 76, 90]
minimum, maximum, avg, count = get_statistics(scores)
print(f"Scores: {scores}")
print(f"Min: {minimum}, Max: {maximum}, Avg: {avg:.2f}, Count: {count}")

# Dengan named tuple untuk clarity
Stats = namedtuple('Stats', ['min', 'max', 'avg', 'count'])

def get_statistics_named(numbers):
    """Return statistics sebagai named tuple"""
    if not numbers:
        return Stats(0, 0, 0, 0)
    
    return Stats(
        min=min(numbers),
        max=max(numbers),
        avg=sum(numbers) / len(numbers),
        count=len(numbers)
    )

stats = get_statistics_named(scores)
print(f"\nNamed tuple result:")
print(f"Min: {stats.min}, Max: {stats.max}, Avg: {stats.avg:.2f}")
print()

# =============================================================================
# 8. USE CASE: KOORDINAT & GEOMETRI
# =============================================================================

print("=== 8. USE CASE: KOORDINAT & GEOMETRI ===")

import math

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['start', 'end'])
Rectangle = namedtuple('Rectangle', ['top_left', 'bottom_right'])

def distance(p1, p2):
    """Hitung jarak antara dua titik"""
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def midpoint(p1, p2):
    """Hitung titik tengah"""
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

def rectangle_area(rect):
    """Hitung luas rectangle"""
    width = abs(rect.bottom_right.x - rect.top_left.x)
    height = abs(rect.bottom_right.y - rect.top_left.y)
    return width * height

# Penggunaan
p1 = Point(0, 0)
p2 = Point(3, 4)
line = Line(p1, p2)
rect = Rectangle(Point(0, 0), Point(10, 5))

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Distance: {distance(p1, p2):.2f}")
print(f"Midpoint: {midpoint(p1, p2)}")
print(f"Rectangle area: {rectangle_area(rect)}")
print()

# =============================================================================
# 9. USE CASE: RGB COLOR
# =============================================================================

print("=== 9. USE CASE: RGB COLOR ===")

Color = namedtuple('Color', ['r', 'g', 'b'])

# Predefined colors
COLORS = {
    "RED": Color(255, 0, 0),
    "GREEN": Color(0, 255, 0),
    "BLUE": Color(0, 0, 255),
    "WHITE": Color(255, 255, 255),
    "BLACK": Color(0, 0, 0),
    "YELLOW": Color(255, 255, 0),
    "CYAN": Color(0, 255, 255),
    "MAGENTA": Color(255, 0, 255),
}

def color_to_hex(color):
    """Convert RGB color ke hex string"""
    return f"#{color.r:02x}{color.g:02x}{color.b:02x}"

def blend_colors(c1, c2, ratio=0.5):
    """Blend dua warna"""
    return Color(
        r=int(c1.r * (1 - ratio) + c2.r * ratio),
        g=int(c1.g * (1 - ratio) + c2.g * ratio),
        b=int(c1.b * (1 - ratio) + c2.b * ratio)
    )

# Penggunaan
print(f"RED: {COLORS['RED']} -> {color_to_hex(COLORS['RED'])}")
print(f"GREEN: {COLORS['GREEN']} -> {color_to_hex(COLORS['GREEN'])}")

blended = blend_colors(COLORS['RED'], COLORS['BLUE'])
print(f"RED + BLUE blend: {blended} -> {color_to_hex(blended)}")
print()

# =============================================================================
# 10. USE CASE: DATABASE RECORD
# =============================================================================

print("=== 10. USE CASE: DATABASE RECORD ===")

# Simulasi database record
User = namedtuple('User', ['id', 'username', 'email', 'created_at'])
Product = namedtuple('Product', ['id', 'name', 'price', 'stock'])
Order = namedtuple('Order', ['id', 'user_id', 'product_id', 'quantity', 'total'])

# Sample data
users = [
    User(1, "alice", "alice@email.com", "2024-01-15"),
    User(2, "bob", "bob@email.com", "2024-01-20"),
    User(3, "charlie", "charlie@email.com", "2024-02-01"),
]

products = [
    Product(101, "Laptop", 15000000, 10),
    Product(102, "Mouse", 250000, 50),
    Product(103, "Keyboard", 500000, 30),
]

# Print users
print("Users:")
for user in users:
    print(f"  {user.id}: {user.username} ({user.email})")

print("\nProducts:")
for product in products:
    print(f"  {product.id}: {product.name} - Rp{product.price:,} (Stock: {product.stock})")

# Query-like operation
expensive_products = [p for p in products if p.price > 300000]
print(f"\nExpensive products (>300k): {[p.name for p in expensive_products]}")
print()

print("=== SELESAI ===")
