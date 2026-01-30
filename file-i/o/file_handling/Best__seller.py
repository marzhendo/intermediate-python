import csv

# Buka file daftar buku (file CSV)
csv_file_path = 'Bestseller - Sheet1.csv'

best_selling_book = None
max_sales = 0

# Tugas 1: Membaca file CSV
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Lewati baris header (judul kolom)
    csv_file.readline()
    
    for row in csv_reader:
        # Ambil data penjualan dari baris (kolom ke-5 berisi 'penjualan dalam jutaan')
        current_sales = float(row[4])
        
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row

# Tugas 2: Membuat file baru untuk menyimpan info buku terlaris
output_file_path = 'bestseller_info.csv'
with open(output_file_path, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    
    # Tulis baris header
    csv_writer.writerow(['Judul Buku', 'Penulis', 'Penjualan (dalam Jutaan)'])
    
    # Tulis informasi buku terlaris
    csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])

# Bonus: Cetak pesan konfirmasi
print('Info buku terlaris berhasil ditulis ke', output_file_path)