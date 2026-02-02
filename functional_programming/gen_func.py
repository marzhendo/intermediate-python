def generator_sederhana():
    yield "Satu"
    yield "Dua"
    yield "Tiga"

# gen = generator_sederhana()
# print(next(gen))  # Output: Satu
# print(next(gen))  # Output: Dua
# print(next(gen))  # Output: Tiga
# print(next(gen))  # Ini akan menimbulkan error StopIteration karena tidak ada item lagi dalam generator

def generator_abadi():
    angka = 0
    while True:
        yield angka
        angka += 1
for i in generator_abadi():
    if i >= 21:
        break
    print(i)  # Output: 0 hingga 19