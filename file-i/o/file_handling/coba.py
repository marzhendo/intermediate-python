try:
    umur = int(input("Masukkan umur Anda: "))
    print(f"Umur anda adalah {umur} tahun")
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
finally:
    print("Program selesai.")