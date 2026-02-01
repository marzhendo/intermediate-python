import functools

transaksi = [100000, -50000, 200000, 50000, -20000]

# Filter untuk mendapatkan hanya transaksi positif (pemasukan)
pemasukan = list(filter(lambda x: x > 0, transaksi))
print(f'Pemasukan: {pemasukan}')  # Output: Pemasukan: [100000, 200000, 50000]
# Tambakan pajak 10% ke setiap transaksi dengan map
transaksi_dengan_pajak = list(map(lambda x: x * 1.1, pemasukan))
print(f'Transaksi dengan pajak: {transaksi_dengan_pajak}')
# Total pendapatan akhir
total_pendapatan = functools.reduce(lambda x, y: x + y, transaksi_dengan_pajak)
print(f'Total pendapatan akhir: {total_pendapatan}')

# List Comprehension untuk mendapatkan transaksi positif dengan pajak
transaksi_akhir = sum(item * 1.1 for item in transaksi if item > 0) # Jika [] dihapus menggunakan () maka disebut generator expression
print(f'Transaksi akhir dengan list comprehension: {transaksi_akhir}') # Generator expression lebih efisien dalam penggunaan memori