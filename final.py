morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

print("Welcome to the Morse Code Translator!")

while True:

    user_data = input('Please write what you want to translate into Morse code (type "exit" to quit): ')

    if user_data.lower() == 'exit':
        print('Goodbye!')
        break   # Exit the loop

    translated_data = []

    # Loop through each character in the user input
    for char in user_data:
        try:
            # Translate the character to morse code and append to the 'translated_data' list
            letter = morse_code[char.upper()]
            translated_data.append(letter)
        # Handling the case where the character is not in the Morse code table
        except KeyError:
            print(f"Sorry, I can't translate '{char}'. ")
            continue    # Skip to the next character

    # Print the translated message in Morse code
    print("Your message translated into Morse Code is:")
    print(' '.join(translated_data))