"""
Python Set - Contoh Penggunaan
===============================
File ini berisi contoh-contoh praktis penggunaan Set di Python.
"""

# =============================================================================
# 1. MEMBUAT SET
# =============================================================================

print("=== 1. MEMBUAT SET ===")

# Set kosong - HARUS pakai set(), bukan {}!
empty_set = set()
empty_dict = {}  # Ini dictionary, bukan set!

# Set dengan elemen
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
mixed = {1, "hello", 3.14}  # Tipe campuran OK

# Set otomatis menghapus duplikat
with_duplicates = {1, 2, 2, 3, 3, 3, 4}
print(f"With duplicates input: {{1, 2, 2, 3, 3, 3, 4}}")
print(f"Result: {with_duplicates}")  # {1, 2, 3, 4}

# Set dari list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_set = set(my_list)
print(f"List: {my_list}")
print(f"Set: {unique_set}")
print()

# =============================================================================
# 2. OPERASI DASAR
# =============================================================================

print("=== 2. OPERASI DASAR ===")

colors = {"red", "green", "blue"}
print(f"colors: {colors}")

# Menambah elemen
colors.add("yellow")
print(f"Setelah add 'yellow': {colors}")

colors.update(["purple", "orange"])
print(f"Setelah update: {colors}")

# Menghapus elemen
colors.remove("yellow")  # Error jika tidak ada
print(f"Setelah remove 'yellow': {colors}")

colors.discard("pink")  # Tidak error jika tidak ada
print(f"Setelah discard 'pink' (tidak ada): {colors}")

popped = colors.pop()  # Hapus elemen random
print(f"Setelah pop (removed: {popped}): {colors}")
print()

# =============================================================================
# 3. OPERASI MATEMATIKA SET
# =============================================================================

print("=== 3. OPERASI MATEMATIKA SET ===")

# Tim developer
frontend = {"Alice", "Bob", "Charlie", "Diana"}
backend = {"Charlie", "Diana", "Eve", "Frank"}
devops = {"Frank", "Grace", "Henry"}

print(f"Frontend: {frontend}")
print(f"Backend: {backend}")
print(f"DevOps: {devops}")
print()

# UNION - gabungan semua
all_devs = frontend | backend | devops
print(f"Semua developer (Union): {all_devs}")

# INTERSECTION - irisan (ada di keduanya)
fullstack = frontend & backend
print(f"Fullstack (Frontend & Backend): {fullstack}")

# DIFFERENCE - hanya di set pertama
only_frontend = frontend - backend
print(f"Hanya Frontend: {only_frontend}")

only_backend = backend - frontend
print(f"Hanya Backend: {only_backend}")

# SYMMETRIC DIFFERENCE - di salah satu tapi tidak keduanya
specialists = frontend ^ backend
print(f"Specialists (bukan fullstack): {specialists}")
print()

# =============================================================================
# 4. OPERASI PERBANDINGAN
# =============================================================================

print("=== 4. OPERASI PERBANDINGAN ===")

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {1, 2, 3}
set_d = {6, 7, 8}

# Subset
print(f"{set_a} issubset of {set_b}: {set_a.issubset(set_b)}")  # True
print(f"{set_a} <= {set_b}: {set_a <= set_b}")  # True

# Superset
print(f"{set_b} issuperset of {set_a}: {set_b.issuperset(set_a)}")  # True
print(f"{set_b} >= {set_a}: {set_b >= set_a}")  # True

# Equality
print(f"{set_a} == {set_c}: {set_a == set_c}")  # True

# Disjoint (tidak ada elemen yang sama)
print(f"{set_a} isdisjoint with {set_d}: {set_a.isdisjoint(set_d)}")  # True
print(f"{set_a} isdisjoint with {set_b}: {set_a.isdisjoint(set_b)}")  # False
print()

# =============================================================================
# 5. USE CASE: MENGHAPUS DUPLIKAT
# =============================================================================

print("=== 5. USE CASE: MENGHAPUS DUPLIKAT ===")

# Email list dengan duplikat
emails = [
    "alice@email.com",
    "bob@email.com",
    "alice@email.com",  # Duplikat
    "charlie@email.com",
    "bob@email.com",    # Duplikat
    "diana@email.com",
]

print(f"Original emails ({len(emails)} items): {emails}")

# Hapus duplikat
unique_emails = list(set(emails))
print(f"Unique emails ({len(unique_emails)} items): {unique_emails}")

# Hapus duplikat tapi PERTAHANKAN URUTAN (Python 3.7+)
unique_ordered = list(dict.fromkeys(emails))
print(f"Unique (ordered): {unique_ordered}")
print()

# =============================================================================
# 6. USE CASE: MEMBERSHIP TESTING CEPAT
# =============================================================================

print("=== 6. USE CASE: MEMBERSHIP TESTING CEPAT ===")

import time

# Simulasi data besar
large_list = list(range(1000000))
large_set = set(range(1000000))

# Cari elemen terakhir
target = 999999

# Test dengan list
start = time.perf_counter()
found_list = target in large_list
time_list = time.perf_counter() - start

# Test dengan set
start = time.perf_counter()
found_set = target in large_set
time_set = time.perf_counter() - start

print(f"Mencari {target} dalam 1 juta item:")
print(f"  List: {found_list}, waktu: {time_list:.6f} detik")
print(f"  Set:  {found_set}, waktu: {time_set:.6f} detik")
print(f"  Set {time_list/time_set:.0f}x lebih cepat!")
print()

# =============================================================================
# 7. USE CASE: VALIDASI INPUT
# =============================================================================

print("=== 7. USE CASE: VALIDASI INPUT ===")

VALID_STATUS = {"pending", "approved", "rejected", "processing"}
VALID_ROLES = {"admin", "moderator", "user", "guest"}
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "webp"}

def validate_status(status):
    if status not in VALID_STATUS:
        raise ValueError(f"Invalid status '{status}'. Must be one of: {VALID_STATUS}")
    return True

def is_valid_role(role):
    return role in VALID_ROLES

def is_allowed_file(filename):
    extension = filename.rsplit('.', 1)[-1].lower()
    return extension in ALLOWED_EXTENSIONS

# Test
print(f"is_valid_role('admin'): {is_valid_role('admin')}")
print(f"is_valid_role('superuser'): {is_valid_role('superuser')}")

print(f"is_allowed_file('photo.jpg'): {is_allowed_file('photo.jpg')}")
print(f"is_allowed_file('document.pdf'): {is_allowed_file('document.pdf')}")

try:
    validate_status("invalid")
except ValueError as e:
    print(f"Error: {e}")
print()

# =============================================================================
# 8. USE CASE: FINDING COMMON & DIFFERENT
# =============================================================================

print("=== 8. USE CASE: FINDING COMMON & DIFFERENT ===")

# Skill matching untuk job application
job_requirements = {"Python", "SQL", "Git", "Docker", "AWS"}
candidate_a_skills = {"Python", "JavaScript", "Git", "React", "Node.js"}
candidate_b_skills = {"Python", "SQL", "Git", "Docker", "Kubernetes"}

def evaluate_candidate(name, skills, requirements):
    matching = skills & requirements
    missing = requirements - skills
    extra = skills - requirements
    match_percent = len(matching) / len(requirements) * 100
    
    print(f"\n{name}:")
    print(f"  Skills: {skills}")
    print(f"  Matching ({len(matching)}): {matching}")
    print(f"  Missing ({len(missing)}): {missing}")
    print(f"  Extra skills: {extra}")
    print(f"  Match: {match_percent:.0f}%")
    
    return match_percent

print(f"Job Requirements: {job_requirements}")
score_a = evaluate_candidate("Candidate A", candidate_a_skills, job_requirements)
score_b = evaluate_candidate("Candidate B", candidate_b_skills, job_requirements)

if score_a > score_b:
    print("\n🏆 Candidate A lebih cocok!")
else:
    print("\n🏆 Candidate B lebih cocok!")
print()

# =============================================================================
# 9. USE CASE: FILE COMPARISON
# =============================================================================

print("=== 9. USE CASE: FILE COMPARISON ===")

# Simulasi perbandingan file
file1_content = """
line 1
line 2
line 3
line 4
line 5
""".strip().split("\n")

file2_content = """
line 1
line 2 modified
line 3
line 6
line 7
""".strip().split("\n")

set1 = set(file1_content)
set2 = set(file2_content)

common = set1 & set2
only_file1 = set1 - set2
only_file2 = set2 - set1

print(f"File 1 lines: {set1}")
print(f"File 2 lines: {set2}")
print(f"\nCommon lines: {common}")
print(f"Only in File 1: {only_file1}")
print(f"Only in File 2: {only_file2}")
print()

# =============================================================================
# 10. USE CASE: TAG SYSTEM
# =============================================================================

print("=== 10. USE CASE: TAG SYSTEM ===")

class Article:
    def __init__(self, title, tags):
        self.title = title
        self.tags = set(tags)
    
    def add_tag(self, tag):
        self.tags.add(tag)
    
    def remove_tag(self, tag):
        self.tags.discard(tag)
    
    def has_tag(self, tag):
        return tag in self.tags
    
    def __repr__(self):
        return f"Article('{self.title}', tags={self.tags})"

# Artikel-artikel
articles = [
    Article("Python Tutorial", ["python", "programming", "tutorial"]),
    Article("Web Development", ["javascript", "web", "programming"]),
    Article("Data Science", ["python", "data", "machine-learning"]),
    Article("DevOps Guide", ["docker", "kubernetes", "devops"]),
]

# Cari artikel dengan tag tertentu
def find_by_tag(articles, tag):
    return [a for a in articles if a.has_tag(tag)]

def find_by_any_tags(articles, tags):
    tags_set = set(tags)
    return [a for a in articles if a.tags & tags_set]

def find_by_all_tags(articles, tags):
    tags_set = set(tags)
    return [a for a in articles if tags_set.issubset(a.tags)]

# Test
print("All articles:")
for article in articles:
    print(f"  {article}")

print("\nArticles with 'python' tag:")
for article in find_by_tag(articles, "python"):
    print(f"  - {article.title}")

print("\nArticles with 'python' OR 'javascript' tag:")
for article in find_by_any_tags(articles, ["python", "javascript"]):
    print(f"  - {article.title}")

print("\nArticles with 'python' AND 'programming' tag:")
for article in find_by_all_tags(articles, ["python", "programming"]):
    print(f"  - {article.title}")

# All unique tags
all_tags = set()
for article in articles:
    all_tags.update(article.tags)
print(f"\nAll unique tags: {sorted(all_tags)}")
print()

# =============================================================================
# 11. FROZEN SET
# =============================================================================

print("=== 11. FROZEN SET ===")

# Frozen set adalah immutable set
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen}")

# Tidak bisa dimodifikasi
try:
    frozen.add(6)
except AttributeError as e:
    print(f"Cannot modify frozen set: {e}")

# Bisa jadi dictionary key
cache = {
    frozenset({1, 2}): "result for {1, 2}",
    frozenset({3, 4}): "result for {3, 4}",
}
print(f"Cache: {cache}")
print(f"Lookup frozenset({{1, 2}}): {cache[frozenset({1, 2})]}")

# Set of sets (harus frozen)
set_of_sets = {frozenset({1, 2}), frozenset({3, 4}), frozenset({5, 6})}
print(f"Set of sets: {set_of_sets}")
print()

print("=== SELESAI ===")
