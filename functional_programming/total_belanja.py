import functools

harga = [5000, 2000, 3000]

def tambah(x, y):
    return x + y

total = functools.reduce(tambah, harga)
print("Total belanjaan:", total)  # Output: Total belanjaan: 10000

# Alternatif menggunakan lambda
total_lambda = functools.reduce(lambda x, y: x + y, harga)
print("Total belanjaan (lambda):", total_lambda)  # Output: Total bel