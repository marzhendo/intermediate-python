list = [
    "I want to win.\n",
    "I want to be a programmer.\n",
    "My name is Pongo.\n"
]

list2 = [
    "I want to be rich.\n",
    "I want to be a programmer.\n",
    "My name is Pongo.\n"
]

file = open("new_book.txt", "w")
file.writelines(list)
file.close()

file = open("new_book.txt", "a")
file.writelines(list2)
file.close()

file = open("new_book.txt", "r")
print(file.readlines())

