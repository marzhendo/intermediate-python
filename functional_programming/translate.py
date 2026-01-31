def translator(language):
    translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}
    def translate_word(word):
        return translations.get(language, {}).get(word, word)
    return translate_word

# Example usage:
translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello'))  # Output: hola