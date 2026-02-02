"""
Decorator adalah fungsi yang membungkus fungsi lain
untuk menambahkan fitur tambahan sebelum atau sesudah fungsi asli dijalankan.
"""
# def say_hello():
#     return "Hello there!"

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("--- Sebelum fungsi dipanggil ---")
        result = (func(*args, **kwargs)) # *args dan **kwargs untuk menangani argumen dinamis
        print(result)
        print("--- Sesudah fungsi dipanggil ---")
        return result
    return wrapper

# decorated_hello = my_decorator(say_hello)
# decorated_hello()  # Memanggil fungsi yang telah dihias

# Syntatic sugar untuk decorator
# Tulis ulang definisi fungsi say_hello dengan tambahan syntatic sugar
@my_decorator
def say_hello(nama):
    return f"Hello {nama}!"
say_hello("Budi")  # Memanggil fungsi yang telah dihias dengan syntatic sugar

pesan = say_hello("Budi")
print(f"Isi variabel pesan: {pesan}")  # Ini akan mencetak None karena wrapper tidak mengembalikan nilai