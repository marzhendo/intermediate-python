import csv

csv_path = 'Bestseller - Sheet1.csv'

with open(csv_path, mode = 'r', encoding = 'utf-8') as file:
    reader = csv.reader(file)
    header = next(reader) # Lewati baris header
    def cari_buku_penjualan_terbanyak(csv_reader):
        penjualan_terbanyak = 0.0
        buku_terlaris = None
        for baris in csv_reader:
            penjualan_saat_ini = float(baris[4])
            if penjualan_saat_ini > penjualan_terbanyak:
                penjualan_terbanyak = penjualan_saat_ini
                buku_terlaris = baris
            return buku_terlaris
    buku_terlaris = cari_buku_penjualan_terbanyak(reader)
    if buku_terlaris:
        print(f"Buku terlaris adalah '{buku_terlaris[0]}' oleh {buku_terlaris[1]} dengan penjualan {buku_terlaris[4]} juta.")
with open('buku_terlaris.csv', mode='w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(header) # Tulis header
    if buku_terlaris:
        csv_writer.writerow(buku_terlaris) # Tulis data buku terlaris
    