text = input('What is your text:')
letters_to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D':'-..',
                 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..',
}
def text_to_morse(text):

    translation = []
    for i in text:
        i = i.upper()
        if i in letters_to_morse:
            translation.append(letters_to_morse.get(i))
        elif i == ' ':
            translation.append('/')
    final_translation = ' '.join(translation)        
    return final_translation


print(F'{text_to_morse(text)} /({text})')


