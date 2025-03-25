
import csv
from InquirerPy import inquirer
import matplotlib.pyplot as mpl
import numpy
import pandas
from faker import Faker
import random
fake = Faker()
#Allows the user to create a character
def create():
    while True:
        match = False
        #Ensures the user picks a name no previous character has.
        name = input("What is the name of your character? If you would like to generate a random name, hit enter without typing anything.\n").strip()
        if name == '':
            name = fake.name()
            print(f'Your character is now named: {name}.')
        chars = get_chars_panda()
        for i in chars.loc[:,'Name']:
            if i == 'name':
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
                save_char(name, input_class, 1, 0, 'No Backstory')
                print("Character saved!")
                return
            elif verify == 'N':
                break
            else:
                print("Please enter y or n.")
                continue

#Saves the character to the csv file
def save_char(name, char_class, level, exp, backstory):
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
        character  =  [name, health, strength, defense, speed, char_class, level, exp, backstory]
        csv_writer.writerow(character)

#Displays all character currently in the list
def display_chars():
    chars = get_chars_panda()
    for idx, i in chars.iterrows():
        print(f'\n{i["Name"]}:\nLevel:{i['Level']}\nEXP:{i['EXP']}\nClass:{i['Class']}\nHealth:{i['Health']}\nAttack:{i['Attack']}')
        print(f'Defense:{i['Defense']}\nSpeed:{i['Speed']}\nBackstory:{i['Backstory']}')

#Returns a DataFrame with all the characters
def get_chars_panda():
    chars = pandas.read_csv('Battle Simulator/chars.csv')
    return chars

#Selects the two characters to battle
def char_select():
    chars = get_chars_panda()
    names = chars.loc[:,'Name']
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
            chars.insert(0, 'Lawsuit', False)
            for idx, i in chars.iterrows():
                if i['Name'] == strchar_one:
                    char_one = i.copy()
                if i['Name'] == strchar_two:
                    char_two = i.copy()
            return [char_one, char_two]
    except:
        print("Please create more than one character before battling.")
        return False
    
#Rewrites the CSV file replacing the old character with the updated character
def edit_char(char,exp_gain):
    chars = get_chars_panda()
    selected = []
    for idx, i in chars.iterrows():
        #Adds all but the selected character to a list
        if i['Name'] != char['Name']:
            selected.append(i)
    with open('Battle Simulator/chars.csv', 'w',newline='') as file:
        csv_writer = csv.writer(file)
        #Writes selected characters back onto the csv
        csv_writer.writerow(['Name','Health','Attack','Defense','Speed','Class','Level','EXP','Backstory'])
        for i in selected:
            csv_writer.writerow(i)
        #Updates and then adds the character that needed updated
    char['EXP'] = str(int(char['EXP']) + exp_gain)
    while True:
        if int(char['EXP']) >= 100:
            char['EXP'] = int(char['EXP']) - 100
            char['Level'] = str(int(char['Level']) + 1)
        else:
            break
    save_char(char['Name'],char['Class'],char['Level'],char['EXP'],char['Backstory'])

#Allows the user to remove a character
def remove():

    #Rewrites the CSV file with all but the selected character.
    def delete_char(str_char):
        chars = get_chars_panda()
        selected = []
        for idx, i in chars.iterrows():
            if i['Name'] != str_char:
                selected.append(i)
        with open('Battle Simulator/chars.csv', 'w',newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Name','Health','Attack','Defense','Speed','Class','Level','EXP','Backstory'])
            for i in selected:
                csv_writer.writerow(i)

    chars = get_chars_panda()
    names = chars.loc[:,'Name']
    char = inquirer.select(
        message="Select a character:",
        choices=names.copy(),
        default=None,
        ).execute()
    delete_char(char)

#Displays a bar graph with character stats
def stat_bars(char):
    #Creates the plot basis
    fig, ax = mpl.subplots()
    #Sets the x and y values to be displayed
    x = [f'Health ({char['Health']})', f'Attack ({char['Attack']})', f'Defense ({char['Defense']})', f'Speed ({char['Speed']})']
    y = [int(char['Health'])/10, int(char['Attack']), int(char['Defense'])*2.5, int(char['Speed'])]
    #creates bar graph using provided data
    ax.bar(x, y)
    #Because stats aren't on the same scales (ie. Health is much higher than the other stats and defense is lower) 
    #so the numbers would be confusing and are removed.
    ax.set_yticklabels([])
    #Titles it based on the character's name
    ax.set_title(f"{char['Name']}'s Stats")
    #Displays the graph
    mpl.show()

def display_stat_bars():
    print("\nThis will display a bar graph for your selected character.")
    print("Because stats aren't on the same scales (ie. Health is much higher than the other stats and defense is lower),")
    print("true stat values are displayed next to the stat's name, while the bars represent the stat relative to your other stats.\n")
    chars = get_chars_panda()
    names = chars.loc[:,'Name']
    name = inquirer.select(
            message="Select a character:",
            choices=names.copy(),
            default=None,
            ).execute()
    for idx, i in chars.iterrows():
        if i['Name'] == name:
            stat_bars(i)
            return
        
def backstories():
    chars = get_chars_panda()
    names = chars.loc[:,'Name']
    name = inquirer.select(
            message="Select a character to generate a new backstory for:",
            choices=names.copy(),
            default=None,
            ).execute()
    for idx, i in chars.iterrows():
        if i['Name'] == name:
            backstory = f'{name} works at {fake.company()} as a {fake.job()}. As a child they wanted to be a(n) {fake.job()}. Their favorite number is {random.randint(-500, 500)},\n and their social security number is {fake.ssn()}'
            print(backstory)
            return backstory, i 
        
def raw_stats(chars):
    mean = round(chars.mean(numeric_only=True), 3)
    print(f'Means across all characters:\nHealth: {mean['Health']}\nAttack: {mean['Attack']}\nDefense: {mean['Defense']}\nSpeed: {mean['Speed']}')
    median = round(chars.median(numeric_only=True))
    print(f'Medians across all characters:\nHealth: {median['Health']}\nAttack: {median['Attack']}\nDefense: {median['Defense']}\nSpeed: {median['Speed']}')
    mode = round(chars.mode(numeric_only=True))
    print(f'Modes across all characters:\nHealth: ')
    for m in mode['Health']:
        print(m, end = ', ')
    print('\nAttack: ')
    for m in mode['Attack']:
        print(m, end = ', ')
    print('\nDefense: ')
    for m in mode['Defense']:
        print(m, end = ', ')
    print('\nSpeed: ')
    for m in mode['Speed']:
        print(m, end = ', ')
    max = round(chars.max(numeric_only=True))
    print(f'\nMaxima across all characters:\nHealth: {max['Health']}\nAttack: {max['Attack']}\nDefense: {max['Defense']}\nSpeed: {max['Speed']}')
    min = round(chars.min(numeric_only=True))
    print(f'Minima across all characters:\nHealth: {min['Health']}\nAttack: {min['Attack']}\nDefense: {min['Defense']}\nSpeed: {min['Speed']}')

#Displays stats on plots gbc = group by class
def plot_stats(col, gbc, chars):
    if col == 'All':
        chars.plot.box()
    elif gbc == 'Yes':
        chars.plot.box(column=col, by='Class')
    else:
        chars.plot.box(column=col)
    mpl.show()

def stat_displays():
    chars = get_chars_panda()
    choice = inquirer.select(
        message="How would you like to view your characters' stats?",
        choices=['Plots', 'Raw Data', 'Exit'],
        default=None,
        ).execute()
    if choice == 'Plots':
        gbc = 'No'
        column = inquirer.select(
            message="Which stat would you like to plot?",
            choices=['Health', 'Attack', 'Defense', 'Speed', 'All'],
            default=None,
            ).execute()
        if column != 'All':
            gbc = inquirer.select(
                message="Would you like to group by classes?",
                choices=['Yes', 'No'],
                default=None,
                ).execute()
        plot_stats(column, gbc, chars)
    elif choice == 'Raw Data':
        raw_stats(chars)
    else:
        return