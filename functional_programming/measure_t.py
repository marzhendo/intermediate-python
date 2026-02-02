import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Waktu eksekusi {func.__name__}: {end - start} detik")
        return result
    return wrapper


@measure_time
def hitung_juta():
    total = sum(range(1, 1000001))
    return total
hitung_juta()
@measure_time
def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial(n - 1)
hitung_faktorial(10)