# Konsep Closure dalam Python
"""
Definisi:
    Closure adalah fungsi yang "mengingat" variabel-variabel
    di lingkungan tempat ia dibuat, bahkan setelah fungsi
    pembuatnya selesai dieksekusi.
    Bayangkan dia membawa "koper" berisi data kemana pun dia pergi. 🧳
"""
translations = {
    "spanish": {"hello": "hola", "bye": "adios"},
    "french": {"hello": "bonjour", "bye": "au revoir"}
}

def create_translator(language):
    def translate(word):
        if language in translations and word in translations[language]:
            return translations[language][word]
        else:
            return f"[No translation for '{word}' in '{language}']"
    return translate

# Membuat penerjemah untuk bahasa Spanyol
translate_to_spanish = create_translator("spanish")
translate_to_french = create_translator("french")
print(translate_to_spanish("hello"))  
print(translate_to_french("hello"))  