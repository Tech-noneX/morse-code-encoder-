
# Dictionary for translating normal letters into Morse code.
# The keys are letters, and the values are Morse symbols.
letters_to_morse: dict[str, str] = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D':'-..',
                 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..',
}


def morse_menu() -> None: 
    """Show the Morse encoder menu and handle the user's choices."""
    # Keep showing the menu until the user chooses to quit.
    while True:   
        print('Option 1: Text to morse')
        print('Option 2: Morse to text')
        print('for Option 1 enter 1, for option 2 enter 2.')
        print('To quit enter q')

        # Clean the menu choice so spaces and uppercase Q do not cause problems.
        user_option: str = input(':').lower().strip()

        if user_option == '1':
            user_text: str = input('Enter your text.\n:').upper()
            # text_to_morse returns the translation, so the menu prints it.
            print(text_to_morse(user_text))
        elif user_option == '2':
            print("each code separate by 'space', words separate by '/'")
            user_morse: str = input('Enter morse code\n:').upper()
            # morse_to_text returns the translation, so the menu prints it.
            print(morse_to_text(user_morse))
        elif user_option == 'q':
            break
        else:
            print('entered input not recognized')
            continue


def morse_to_text(user_morse) -> str:
    """Translate Morse code into normal text."""
    
    spaced_morse: str = user_morse.replace('/', ' / ')
    cleaned_morse: list[str] = spaced_morse.split()
    translation: list[str] = []
    # Reverse lookup: compare the user's Morse code with dictionary values.
    # When the value matches, append the matching key, which is the normal letter.
    for i in cleaned_morse:
        if i == '/':
            translation.append(' ')
            continue

        for letter, morse_code in letters_to_morse.items():
            if morse_code == i:
                translation.append(letter)
                break
        if i not in letters_to_morse.values():
            translation.append('&')
        
                        
    final_translation: str = ''.join(translation)
    return final_translation   


def text_to_morse(user_text) -> str:
    """Translate normal text into Morse code."""
    # Store each Morse symbol before joining them into one string.
    translation: list[str] = []

    # Translate each character from the user's text into Morse code.
    for i in user_text:
        i = i.upper()
        if i in letters_to_morse:
            translation.append(letters_to_morse.get(i))
        elif i == ' ':
            # Use / to show a word gap in Morse code.
            translation.append('/')
        else:
            translation.append('&')
    morse_translation = ' '.join(translation)        
    return morse_translation


# Only start the menu when this file is run directly.
# This prevents the menu from starting automatically if the file is imported.
if __name__ == "__main__":
    morse_menu()


#print(F'{text_to_morse(text)} /({text})')


