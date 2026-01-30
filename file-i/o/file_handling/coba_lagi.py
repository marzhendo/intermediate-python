try:
    file = open("angka.txt", "r")
    isi = int(file.read())
    print(f"Hasil dari file ini adalah {isi}")
except ValueError:
    print("File tidak valid")
except FileNotFoundError:
    print("File tidak ditemukan")
finally:
    print("Program selesai")
    file.close()

