# pure function
from math import pi
def pure_calculate_area(radius):
    return pi * radius ** 2

# impure function
def impure_calculate_area(radius):
    print(f'The area of the circle with radius {radius} is {pi * radius ** 2}')
    return pi * radius ** 2

impure_calculate_area(5)
result = pure_calculate_area(5)
print(f'Pure function result: {result}')

# pure function of luas

def pure_hitung_luas(panjang, lebar):
    return panjang * lebar

def kuadrat(x):
    return x * x

# higher-order function

angka = [1, 2, 3, 4, 5]

list_kuadrat = list(map(kuadrat, angka))

print(f'List kuadrat: {list_kuadrat}')