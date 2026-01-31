def translator(language):
    translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}
    def translate_word(word):
        if language not in translations:
            print("Translation not available")
            return word
        if word in translations[language]:
            return translations[language][word]
        else:
            print(f'The word "{word}" is not available in {language} translations.')
            return word
        
    return translate_word

# Example usage:
translate_to_french = translator('french')
print(translate_to_french('goodbye'))  # Output: au revoir
translate_to_sunda = translator('sunda')
print(translate_to_sunda('hello'))  # Output: Translation not available \n hello