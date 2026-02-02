"""List comprehension adalah konsep dalam pemrograman fungsional yang memungkinkan pembuatan daftar baru dengan cara yang lebih ringkas dan ekspresif dibandingkan dengan penggunaan fungsi map() dan filter()."""

angka = [10, 22, 13, 45, 67, 89, 90, 34, 23, 11]

# Menggunakan list comprehension untuk mendapatkan angka genap
angka_genap = [x for x in angka if x % 2 == 0]
print(angka_genap)  # Output: [10, 22, 90, 34]
# Menggunakan list comprehension untuk mendapatkan angka ganjil
angka_ganjil = [x for x in angka if x % 2 != 0]
print(angka_ganjil)  # Output: [13, 45, 67, 89, 23, 11]
# Menggunakan list comprehension untuk mengkuadratkan setiap angka dalam daftar
kuadrat_angka = [x ** 2 for x in angka]
print(kuadrat_angka)  # Output: [100, 484, 169, 2025, 4489, 7921, 8100, 1156, 529, 121]
# Menggunakan list comprehension untuk menambahkan 5 pada setiap angka dalam daftar
tambah_lima = [x + 5 for x in angka]
print(tambah_lima)  # Output: [15, 27, 18, 50, 72, 94, 95, 39, 28, 16]
# Menggunakan list comprehension untuk mengalikan setiap angka dalam daftar dengan 2
kali_dua = [x * 2 for x in angka]
print(kali_dua)  # Output: [20, 44, 26, 90, 134, 178, 180, 68, 46, 22]
# Menggunakan list comprehension untuk mendapatkan angka lebih dari 50
lebih_dari_lima_puluh = [x for x in angka if x > 50]
print(lebih_dari_lima_puluh)  # Output: [67, 89, 90]
# Menggunakan list comprehension untuk mendapatkan angka kurang dari atau sama dengan 20
kurang_dari_sama_dengan_dua_puluh = [x for x in angka if x <= 20]
print(kurang_dari_sama_dengan_dua_puluh)  # Output: [10, 13, 11]
# Menggunakan list comprehension untuk mendapatkan angka antara 20 dan 50
antara_dua_puluh_dan_lima_puluh = [x for x in angka if 20 < x < 50]
print(antara_dua_puluh_dan_lima_puluh)  # Output: [22, 34, 23]
# Menggunakan list comprehension untuk mendapatkan angka yang merupakan kelipatan dari 3
kelipatan_tiga = [x for x in angka if x % 3 == 0]
print(kelipatan_tiga)  # Output: [45, 90]