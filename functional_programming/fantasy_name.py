import random
import functools
prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
    # Mengubah huruf pertama suffix menjadi kapital menggunakan map()
    return name.capitalize()

capitalized_suffixes = list(map(capitalize_suffix, suffixes))
print(capitalized_suffixes)  # Output: ['Storm', 'Song', 'Fire', 'Blade', 'Whisper']
    
def create_fantasy_name(list1, list2):
    # Menggabungkan prefix dan suffix untuk membuat nama fantasi menggunakan list comprehension
    return random.choice(list1) + ' ' + random.choice(list2)

random_names = [create_fantasy_name(prefixes, capitalized_suffixes) for _ in range(10)]
print(random_names)  

def fire_in_name(name):
    return 'Fire' in name

def concatenate_names(name1, name2):
    return name1 + ' & ' + name2

filtered_names = list(filter(fire_in_name, random_names))
reduced_names = functools.reduce(concatenate_names, filtered_names) if filtered_names else 'No names with Fire found'

def display_name_info():
    print("Generated Fantasy Names:")
    for name in random_names:
        print(name)
    print("\nNames containing 'Fire':")
    for name in filtered_names:
        print(name)
    print("\nReduced Name:")
    print(reduced_names)

display_name_info()