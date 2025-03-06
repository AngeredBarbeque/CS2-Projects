
import csv
#Allows the user to create a character
def create():
    while True:
        name = input("What is the name of your character?\n")
        print("What class is your character?\n1:Mumified Dog: Boosted defense\nPreserve: Preserve yourself in a peat bog in order to boost your defense for 3 turns.\nAt Level 5: Arson: launch a flaming ball of swamp matter dealing damage that ignores defense.")
        print("2:Lawyer: Boosted speed\nLawsuit: Sues the oppenent, inflicting them with crippling debt, which deals damage every turn.\nAt Level 5: Reverse Jury Nullification: Falsely convicts the oppenent, dealing considerable damage.")
        print("3:Pig: Boosted strength\nCharge: Headbutts the oppenent, dealing damage with a chance to stun.\nAt Level 5: Eat Scraps: Eats a pile of trash in order to regain health.")
        print('4:Exit')
        input_class = input('Choose:').strip()
        if input_class == '1':
            char_class = 'Mummified Dog'
        elif input_class == '2':
            char_class = 'Lawyer'
        elif input_class == '3':
            char_class = 'Pig'
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
    health = 100
    strength = 10
    defense = 4
    speed = 10
    #Edits the  player's stats based on their level and class
    if char_class == 'Mummified Dog':
        defense = round(defense * 1.5)
    elif char_class == 'Lawyer':
        speed = round(speed * 1.5)
    elif char_class == 'Pig':
        strength = round(strength * 1.5)
    for i in range(level - 1):
        health = round(health * 1.2)
        strength = round(strength * 1.2)
        defense  =  round(defense * 1.2)
        speed = round(speed * 1.2)
    with open('Battle Simulator/chars.csv', 'a',newline='') as file:
        csv_writer = csv.writer(file)
        character  =  [name, health, strength, defense, speed, char_class, level, exp]
        csv_writer.writerow(character)

#Displays all character currently in the list
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