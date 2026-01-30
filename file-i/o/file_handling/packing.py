import csv

data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]

try:
    with open('packing_list.csv', mode = 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'{row[0]}: {row[1]}')
except FileNotFoundError:
    print("File not found. Creating a new packing list.")
    with open('packing_list.csv', mode = 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Packing list created.")
    print("Please run the program again to read the packing list.")
finally:
    print("Execution completed.")