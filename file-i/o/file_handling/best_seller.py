"""
Docstring for file-i.o.file_handling.best_seller

 Use the CSV reader to navigate through the data and find the book with the highest sales, via the sales in millions column.
For help with selecting the sales in millions column:

for row in csv_reader:

  current_sales = float(row[4])
  
  if current_sales > max_sales:
    max_sales = current_sales
    best_selling_book = row

And to use .writerow() to edit a CSV file:

csv_writer = csv.writer('example.csv')
csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
"""
import csv

with open('Bestseller - Sheet1.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader) # Skip header row
    max_sales = 0.0
    best_selling_book = None
    for row in csv_reader:
        current_sales = float(row[4])
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row
    if best_selling_book:
        print(f"The best selling book is '{best_selling_book[0]}' by {best_selling_book[1]} with {best_selling_book[4]} million sales.")
with open('best_selling_book.csv', mode='w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(header)  # Write header
    if best_selling_book:
        csv_writer.writerow(best_selling_book)  # Write best selling book data