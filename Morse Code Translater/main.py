#Nicholas Larsen Morse Code Translater

english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
morse = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.', '___', '.__.', '__._', '._.', '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..', '.____', '..___', '...__', '...._', '.....', '_....', '__...', '___..', '____.', '_____']

def morse_to_english(morse, english):
    translated = []
    message = input("What message would you like to translate?\nPlease use . and _, with - surrounded by spaces to represent spaces.\nUse spaces in between letters.\n").lower()
    list_message = message.split(' ')
    for i in list_message:
        for item in morse:
            if i == item:
                translated.append(english[morse.index(item)])
            elif i == '-':
                translated.append(' ')
                break
    translated_str = ''.join(translated)
    print(translated_str)

def english_to_morse(morse, english):
    translated = []
    message = input("What message would you like to translate?").lower()
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



def main():
    print("Welcome to your morse code translater!")
    while True:
        choice = input("Would you like to:\n1:Translate English to morse code\n2:Translate morse code to English\n3:Exit\n")
        if choice == '1':
            english_to_morse(morse, english)
        elif choice == '2':
            morse_to_english(morse, english)
        elif choice == '3':
            print("Goodbye!")
            exit()
        else:
            print("Sorry, please enter 1, 2, or 3.")
            continue
main()