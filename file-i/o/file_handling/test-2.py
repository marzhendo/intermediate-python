import csv

data_siswa = [
    ["Nama", "Kelas"],
    ["Ali", "10A"],
    ["Siti", "11E"]
]

try:
    with open("siswa.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data_siswa)
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
finally:
    print("Program selesai.")