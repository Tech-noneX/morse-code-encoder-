
letters_to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D':'-..',
                 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..',
}
def morse_menu():
    while True:   
        print('Option 1: Text to morse')
        print('Option 2: Morse to text')
        print('for Option 1 enter 1, for option 2 enter 2.')
        print('To quit enter q')
        user_option = input(':')
        if user_option == '1':
            user_text = input('Enter your text.\n:')
            text_to_morse(user_text)
        elif user_option == '2':
            print("each code separate by 'space', words separate by '/'")
            user_morse = input('Enter morse code')
            morse_to_text(user_morse)
        elif user_option == 'q':
            break
        else:
            print('entered input not recognized')
            continue
def morse_to_text(user_morse):
    
    translation =[]
    for i in user_morse:
        for key, value in letters_to_morse.items():
            if value == i:
                translation.append(key)
        


def text_to_morse(user_text):
    
    translation = []
    for i in user_text:
        i = i.upper()
        if i in letters_to_morse:
            translation.append(letters_to_morse.get(i))
        elif i == ' ':
            translation.append('/')
    final_translation = ' '.join(translation)        
    print(final_translation)
 
morse_menu()


#print(F'{text_to_morse(text)} /({text})')


