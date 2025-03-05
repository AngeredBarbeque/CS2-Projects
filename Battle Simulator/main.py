#Allows the user to create a character
def create():
    while True:
        name = input("What is the name of your character?\n")
        print("What class is your character?\n1:Warrior: Boosted defense\n")
        print("2:Rogue: Boosted speed\n")
        print("3:Brute: Boosted strength\n")
        print('4:Exit')
        input_class = input('Choose:').strip()
        if input_class == '1':
            char_class = 'Warrior'
        elif input_class == '2':
            char_class = 'Rogue'
        elif input_class == '3':
            char_class = 'Brute'
        elif input_class == '4':
            return
        else:
            print("Please enter 1, 2, 3 or 4.")
            continue
        while True:
            #Verifies the character
            print(f"{name} the {char_class}.\nIs that correct?")
            verify = input('y/n:').upper()
            if verify == 'Y':
                save_char(name, char_class, 1, 0)
                print("Character saved!")
                return
            elif verify == 'N':
                break
            else:
                print("Please enter y or n.")
                continue

#Saves the character to the csv file
def save_char(name, char_class, level, exp):
    import csv
    health = 100
    strength = 10
    defense = 4
    speed = 10
    #Edits the  player's stats based on their level and class
    if char_class == 'Warrior':
        defense = round(defense * 1.5)
    elif char_class == 'Rogue':
        speed = round(speed * 1.5)
    elif char_class == 'Brute':
        strength = round(strength * 1.5)
    for i in range(level):
        health = round(health * 1.2)
        strength = round(strength * 1.2)
        defense  =  round(defense * 1.2)
        speed = round(speed * 1.2)
    with open('Battle Simulator/chars.csv', 'a',newline='') as file:
        csv_writer = csv.writer(file)
        character  =  [name, health, strength, defense, speed, char_class, level, exp, ]
        csv_writer.writerow(character)
def display_chars():
    chars = []
    with open('Battle Simulator/chars.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for i in csv_reader:
            chars.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
        for i in chars:
            print(f'\n{i[0]}:\nLevel:{i[6]}\nEXP:{i[7]}\nClass:{i[5]}\nHealth:{i[1]}\nStrength:{i[2]}')
            print(f'Defense:{i[3]}\nSpeed:{i[4]}\n')


import csv
display_chars()