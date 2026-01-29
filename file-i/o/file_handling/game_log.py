with open("quest_log.txt", "w") as file:
    file.write("--- Game Dimulai ---")
    file.write("\n")

with open("quest_log.txt", "a") as file:
    file.write("Pemain menemukan Pedang Emas.")
    file.write("\n")
    file.write("Pemain melawan monster.")
    file.write("\n")
    file.write("Pemain menang.")
    file.write("\n")

with open("quest_log.txt", "r") as file:
    print(file.read())

for nomor, baris in enumerate(open("quest_log.txt"), start=1):
    print(f"{nomor}: {baris.strip()}")
