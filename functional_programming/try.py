translate = {
    'jawa': {'hello': 'halo', 'goodbye': 'mulih disik yo', 'thank you': 'suwun lik'},
    'batak': {'hello': 'horas', 'goodbye': 'mauliate', 'thank you': 'tung so marhite'},
    'minang': {'hello': 'halo', 'goodbye': 'sampai jumpa', 'thank you': 'terima kasih'},
    'sunda': {'hello': 'halo', 'goodbye': 'dahar heula', 'thank you': 'hatur nuhun'},
    'mexico': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
    'jamaica': {'hello': 'wa gwaan', 'goodbye': 'lata', 'thank you': 'tank yuh', 'very good': 'bombo clat'},
    'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias', 'my drum': 'mi bombo'},
}

def translator(language):
    def translate_word(word):
        if language not in translate:
            print(f"Translation for '{language}' not available")
            return word
        if word in translate[language]:
            return translate[language][word]
        else:
            print(f'The word "{word}" is not available in {language} translations.')
            return word
    return translate_word

translate_ke_jawa = translator('spanish')
print(translate_ke_jawa('my drum')) 