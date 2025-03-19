
import csv
from InquirerPy import inquirer
import matplotlib.pyplot as mpl
import numpy
#Allows the user to create a character
def create():
    while True:
        match = False
        #Ensures the user picks a name no previous character has.
        name = input("What is the name of your character?\n")
        chars = get_chars()
        for i in chars:
            if i[0] == 'name':
                print("Sorry, another character is already named that.\n")
                continue
        #Prints class options, and then allows user to
        print("What class is your character?\nMumified Dog: Boosted defense\nPreserve: Preserve yourself in a peat bog in order to boost your defense for 3 turns.\nAt Level 5: Arson: launch a flaming ball of swamp matter dealing damage that ignores defense.")
        print("Lawyer: Boosted speed\nLawsuit: Sues the oppenent, inflicting them with crippling debt, which deals damage to them every turn.\nAt Level 5: Reverse Jury Nullification: Falsely convicts the oppenent, dealing considerable damage.")
        print("Pig: Boosted strength\nCharge: Headbutts the oppenent, dealing damage with a chance to crit.\nAt Level 5: Eat Scraps: Eats a pile of trash in order to regain health.")
        print('Exit')
        input_class = inquirer.select(
        message="Select a class:",
        choices=[
            "Mummified Dog",
            "Lawyer",
            'Pig',
            "Exit",
        ],
        default=None,
        ).execute()
        if input_class == 'Exit':
            return
        while True:
            #Verifies the character
            print(f"{name} the {input_class}.\nIs that correct?")
            verify = input('y/n:').upper()
            if verify == 'Y':
                #Saves the character
                save_char(name, input_class, 1, 0)
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
    for i in range(int(level) - 1):
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
    chars = get_chars()
    for i in chars:
        print(f'\n{i[0]}:\nLevel:{i[6]}\nEXP:{i[7]}\nClass:{i[5]}\nHealth:{i[1]}\nStrength:{i[2]}')
        print(f'Defense:{i[3]}\nSpeed:{i[4]}\n')

#Returns a list with all the characters
def get_chars():
    chars = []
    with open('Battle Simulator\chars.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for i in csv_reader:
            chars.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    return chars

#Selects the two characters to battle
def char_select():
    chars = get_chars()
    names = []
    for i in chars:
        names.append(i[0])
    try:
        #Prints a list of all characters and makes the user select two.
        strchar_one = inquirer.select(
            message="Select a character:",
            choices=names.copy(),
            default=None,
            ).execute()
        strchar_two = inquirer.select(
            message="Select another character:",
            choices=names.copy(),
            default=None,
            ).execute()
        if strchar_one == strchar_two:
            print("Please choose two seperate characters.")
            return False
        else:
            char_one = []
            char_two  =  []
            for i in chars:
                if i[0] == strchar_one:
                    char_one = i.copy()
                if i[0] == strchar_two:
                    char_two = i.copy()
            return [char_one, char_two]
    except:
        print("Please create more than one character before battling.")
        return False
    
#Rewrites the CSV file replacing the old character with the updated character
def edit_char(char,exp_gain):
    chars = get_chars()
    selected = []
    for i in chars:
        #Adds all but the selected character to a list
        if i[0] != char[0]:
            selected.append(i)
    with open('Battle Simulator/chars.csv', 'w',newline='') as file:
        csv_writer = csv.writer(file)
        #Writes selected characters back onto the csv
        csv_writer.writerow(['Name','Health','Attack','Defense','Speed','Class','Level','EXP'])
        for i in selected:
            csv_writer.writerow(i)
        #Updates and then adds the character that needed updated
    char[7] = str(int(char[7]) + exp_gain)
    while True:
        if int(char[7]) >= 100:
            char[7] = int(char[7]) - 100
            char[6] = str(int(char[6]) + 1)
        else:
            break
    save_char(char[0],char[5],char[6],char[7])

#Allows the user to remove a character
def remove():

    #Rewrites the CSV file with al but the selected character.
    def delete_char(str_char):
        chars = get_chars()
        selected = []
        for i in chars:
            if i[0] != str_char:
                selected.append(i)
        with open('Battle Simulator/chars.csv', 'w',newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Name','Health','Attack','Defense','Speed','Class','Level','EXP'])
            for i in selected:
                csv_writer.writerow(i)

    chars = get_chars()
    names = []
    for i in chars:
        names.append(i[0])
    char = inquirer.select(
    message="Select a character:",
    choices=names.copy(),
    default=None,
    ).execute()
    delete_char(char)

def stat_bars(char):
    mpl.style.use('_mpl-gallery')
    #uses the stats of the provided character as the numbers for the bar heights.
    #For some reason we need this 0.5, otherwise the graph starts in a weird way, cutting off part of the first one.
    x = 0.5 + numpy.arange(4)
    y = [int(char[1]), int(char[2]), int(char[3]), int(char[4])]
    #Creates a figure and axis
    fig, ax = mpl.subplots()
    #Sets the visuals of the bars
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7, label=['Health', 'Attack', 'Defense', 'Speed'])
    #Arranges the axis
    ax.set(xlim=(0, 8), xticks=numpy.arange(1, 8),
           #Arrange is spelt wrong??
        ylim=(0, 8), yticks=numpy.arange(1, 8))
    #Displays the graph
    mpl.show()
chars = get_chars()
stat_bars(chars[0])