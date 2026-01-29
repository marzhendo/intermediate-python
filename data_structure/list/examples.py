"""
Python List - Contoh Penggunaan
================================
File ini berisi contoh-contoh praktis penggunaan List di Python.
"""

# =============================================================================
# 1. MEMBUAT LIST
# =============================================================================

# List kosong
empty_list = []
empty_list2 = list()

# List dengan elemen
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, None]

# List dari range
numbers_range = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("=== 1. MEMBUAT LIST ===")
print(f"numbers: {numbers}")
print(f"fruits: {fruits}")
print(f"mixed: {mixed}")
print()

# =============================================================================
# 2. MENGAKSES ELEMEN
# =============================================================================

colors = ["red", "green", "blue", "yellow", "purple"]

print("=== 2. MENGAKSES ELEMEN ===")
print(f"colors: {colors}")
print(f"Elemen pertama: {colors[0]}")
print(f"Elemen terakhir: {colors[-1]}")
print(f"Elemen ke-2 sampai ke-4: {colors[1:4]}")
print(f"3 elemen pertama: {colors[:3]}")
print(f"3 elemen terakhir: {colors[-3:]}")
print()

# =============================================================================
# 3. MODIFIKASI LIST
# =============================================================================

todos = ["Belajar Python", "Olahraga", "Makan"]

print("=== 3. MODIFIKASI LIST ===")
print(f"Awal: {todos}")

# Tambah elemen
todos.append("Tidur")
print(f"Setelah append: {todos}")

todos.insert(1, "Sarapan")
print(f"Setelah insert: {todos}")

# Ubah elemen
todos[0] = "Belajar JavaScript"
print(f"Setelah ubah: {todos}")

# Hapus elemen
todos.remove("Olahraga")
print(f"Setelah remove: {todos}")

last_item = todos.pop()
print(f"Setelah pop (item: {last_item}): {todos}")
print()

# =============================================================================
# 4. LIST COMPREHENSION
# =============================================================================

print("=== 4. LIST COMPREHENSION ===")

# Basic comprehension
squares = [x**2 for x in range(1, 11)]
print(f"Kuadrat 1-10: {squares}")

# Dengan kondisi
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(f"Genap 1-20: {even_numbers}")

# Dengan if-else
labels = ["genap" if x % 2 == 0 else "ganjil" for x in range(1, 6)]
print(f"Labels: {labels}")

# Transform string
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Uppercase: {upper_words}")
print()

# =============================================================================
# 5. OPERASI LIST
# =============================================================================

print("=== 5. OPERASI LIST ===")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Concatenation: {combined}")

# Repetition
repeated = [0] * 5
print(f"Repetition: {repeated}")

# Membership
print(f"2 in list1: {2 in list1}")
print(f"9 in list1: {9 in list1}")

# Length
print(f"Length of combined: {len(combined)}")

# Min, Max, Sum
numbers = [5, 2, 8, 1, 9, 3]
print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")
print()

# =============================================================================
# 6. SORTING
# =============================================================================

print("=== 6. SORTING ===")

scores = [85, 92, 78, 95, 88, 76]
print(f"Original: {scores}")

# sorted() - return list baru
sorted_scores = sorted(scores)
print(f"sorted(): {sorted_scores}")
print(f"Original setelah sorted(): {scores}")  # Tidak berubah

# sort() - mengubah list asli
scores.sort()
print(f"Setelah sort(): {scores}")

# Descending
scores.sort(reverse=True)
print(f"Descending: {scores}")

# Sort by custom key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Students by score: {students_sorted}")
print()

# =============================================================================
# 7. USE CASE: SHOPPING CART
# =============================================================================

print("=== 7. USE CASE: SHOPPING CART ===")

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        item = {"name": name, "price": price, "quantity": quantity}
        self.items.append(item)
        print(f"Added: {name} x{quantity}")
    
    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                print(f"Removed: {name}")
                return
        print(f"Item not found: {name}")
    
    def get_total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def show_cart(self):
        print("\n--- Shopping Cart ---")
        for item in self.items:
            subtotal = item["price"] * item["quantity"]
            print(f"{item['name']} x{item['quantity']} = Rp{subtotal:,}")
        print(f"Total: Rp{self.get_total():,}")
        print("--------------------\n")

# Penggunaan
cart = ShoppingCart()
cart.add_item("Laptop", 15000000)
cart.add_item("Mouse", 250000, 2)
cart.add_item("Keyboard", 500000)
cart.show_cart()

cart.remove_item("Mouse")
cart.show_cart()

# =============================================================================
# 8. USE CASE: STACK (LIFO)
# =============================================================================

print("=== 8. USE CASE: STACK (LIFO) ===")

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")
    
    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f"Popped: {item}")
            return item
        print("Stack is empty!")
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Browser history simulation
browser = Stack()
browser.push("google.com")
browser.push("github.com")
browser.push("stackoverflow.com")
print(f"Current page: {browser.peek()}")
browser.pop()  # Back
print(f"After back: {browser.peek()}")
print()

# =============================================================================
# 9. USE CASE: UNDO/REDO
# =============================================================================

print("=== 9. USE CASE: UNDO/REDO ===")

class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []
        self.redo_stack = []
    
    def write(self, new_text):
        self.history.append(self.text)
        self.text = new_text
        self.redo_stack.clear()
        print(f"Text: '{self.text}'")
    
    def undo(self):
        if self.history:
            self.redo_stack.append(self.text)
            self.text = self.history.pop()
            print(f"Undo -> Text: '{self.text}'")
        else:
            print("Nothing to undo")
    
    def redo(self):
        if self.redo_stack:
            self.history.append(self.text)
            self.text = self.redo_stack.pop()
            print(f"Redo -> Text: '{self.text}'")
        else:
            print("Nothing to redo")

editor = TextEditor()
editor.write("Hello")
editor.write("Hello World")
editor.write("Hello World!")
editor.undo()
editor.undo()
editor.redo()
print()

print("=== SELESAI ===")
