#Nicholas Larsen Morse Code Translater

#lists of english characters and corresponding morse code, with indexes matched.
english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
morse = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.', '___', '.__.', '__._', '._.', '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..', '.____', '..___', '...__', '...._', '.....', '_....', '__...', '___..', '____.', '_____']

#translates morse code to english
def morse_to_english(morse, english):
    translated = []
    message = input("What message would you like to translate?\nPlease use . and _, with - surrounded by spaces to represent spaces.\nUse spaces in between letters.\n(Invalid morse code will be ignored.)\n").lower()
    #splits the string into a list
    list_message = message.split(' ')
    #for each character in the list, check if it matches any of the morse code characters, and if it does, add the corresponding english character to the final translated message.
    for i in list_message:
        for item in morse:

            if i == item:
                translated.append(english[morse.index(item)])

            elif i == '-':
                translated.append(' ')
                break

    translated_str = ''.join(translated)
    print(translated_str)

#Translates english to morse code
def english_to_morse(morse, english):
    translated = []
    message = input("What message would you like to translate? (Invalid characters will be ignored.)").lower()
    #for each character in the string, check if it matches any of the english characters, and if it does, add the corresponding more code to the final translated message.
    for i in message:
        for item in english:

            if i == item:
                translated.append(morse[english.index(item)])
                translated.append(' ')

            elif i == ' ':
                translated.append(' - ')
                break

    translated_str = ''.join(translated)
    print(translated_str)


#Allows the user to translate English -> Morse, Morse -> English, or exit.
def morse_main():
    print("Welcome to your morse code translater!")
    while True:

        choice = input("Would you like to:\n1:Translate English to morse code\n2:Translate morse code to English\n3:Exit\n")
        if choice == '1':
            english_to_morse(morse, english)

        elif choice == '2':
            morse_to_english(morse, english)

        elif choice == '3':
            return

        else:
            print("Sorry, please enter 1, 2, or 3.")
            continue