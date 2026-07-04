


letters_to_morse: dict[str, str] = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D':'-..',
                 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..',
}
def morse_menu() -> None: 
    while True:   
        print('Option 1: Text to morse')
        print('Option 2: Morse to text')
        print('for Option 1 enter 1, for option 2 enter 2.')
        print('To quit enter q')
        user_option: str = input(':').lower().strip()
        if user_option == '1':
            user_text: str = input('Enter your text.\n:').upper()
            print(text_to_morse(user_text))
        elif user_option == '2':
            print("each code separate by 'space', words separate by '/'")
            user_morse: str = input('Enter morse code').upper()
            print(morse_to_text(user_morse))
        elif user_option == 'q':
            break
        else:
            print('entered input not recognized')
            continue
def morse_to_text(user_morse) -> str:
    
    translation: list[str] = []
    for i in user_morse:
        for letter, morse_code in letters_to_morse.items():
            if morse_code == i:
                translation.append(letter)
        


def text_to_morse(user_text) -> str:
    
    translation: list[str] = []
    for i in user_text:
        i = i.upper()
        if i in letters_to_morse:
            translation.append(letters_to_morse.get(i))
        elif i == ' ':
            translation.append('/')
    morse_translation = ' '.join(translation)        
    return morse_translation

if __name__ == "__main__":
    morse_menu()


#print(F'{text_to_morse(text)} /({text})')


