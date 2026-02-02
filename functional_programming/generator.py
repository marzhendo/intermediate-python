""" Generator expression adalah konsep yang mirip dengan list comprehension,
tetapi menghasilkan generator yang menghasilkan item satu per satu
daripada membuat seluruh list sekaligus di memori.
Ini lebih efisien dalam penggunaan memori untuk dataset besar.
"""
import sys

list_comp = [i for i in range(1000000)] # List comprehension
gen_exp = (i for i in range(3))  # Generator expression
# print(f'{gen_exp[10]}')  # Ini akan menimbulkan error karena generator tidak mendukung indexing
# Untuk mendapatkan nilai dari generator, kita bisa menggunakan for loop atau fungsi next()
for angka in gen_exp:
    print(angka)
# Menggunakan next() untuk mendapatkan nilai berikutnya dari generator
gen_exp = (i for i in range(3))  # Reset generator
print(next(gen_exp))  # Output: 0

print(f"Ukuran list comprehension: {sys.getsizeof(list_comp)} bytes")
print(f"Ukuran generator expression: {sys.getsizeof(gen_exp)} bytes")

gen_exp = (h for h in "ABC")  # Generator expression dari string
print(next(gen_exp))  # Output: 'A'
print(next(gen_exp))  # Output: 'B'
print(next(gen_exp))  # Output: 'C'
print(next(gen_exp))  # Ini akan menimbulkan error StopIteration karena tidak ada item lagi dalam generator
