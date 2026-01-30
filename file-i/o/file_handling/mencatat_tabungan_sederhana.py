try:
    print("Mau nabung berapa hari ini?")
    uang = int(input("Masukkan jumlah uang: "))
    with open("tabungan.txt", "a") as file:
        file.write(f"{uang}\n")
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
finally:
    print("Program selesai.")