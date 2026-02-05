def inbox_user():
    yield "Halo, apa kabar?"
    yield "SELAMAT! Anda menang lotere! Klik di sini!"
    yield "Besok kita meeting jam 9 ya."

def filter_spam(func):
    def wrapper():
        for message in func():
            if "lotere" in message.lower():
                continue
            else:
                yield message
    return wrapper

@filter_spam
def inbox_user():
    yield "Halo, apa kabar?"
    yield "SELAMAT! Anda menang lotere! Klik di sini!"
    yield "Besok kita meeting jam 9 ya."

for msg in inbox_user():
    print(msg)