from character_management import *
import random
#Runs a battle, eventually returning the exp gain of the character that won
def battle():
    def turn(char, oppenent):
        health = char[1]
        oppenent_health = oppenent[1]
        #Gives the player their deserved abilities
        if char[5] == 'Pig':
            abilities = ['Headbutt']
            if int(char[6]) >= 5:
                abilities.append('Eat Scraps')
        elif char[5] == 'Lawyer':
            abilities = ['Lawsuit']
            if int(char[6]) >= 5:
                abilities.append('Reverse Jury Nullification')
        elif char[5] == 'Mummified Dog':
            abilities = ['Preserve']
            if int(char[6]) >= 5:
                abilities.append('Arson')
        choice = inquirer.select(
            message="Select an action:",
            choices=['Normal Strike'].append(abilities),
            default=None,
            ).execute()
        if choice == 'Normal Strike':
            damage = char[2] - oppenent[3]
            oppenent_health -= damage
        elif choice == 'Headbutt':
            if random.randint(1, 5) == 5:
                damage = char[2] * 1.5 - oppenent[3]
            else:
                damage = char[2] - oppenent[3]
        elif choice == 'Eat Scraps':
            health += health * 0.2

            #NEED TO ADD STATUS CONDITIONS AND REST OF ABILITIES

    char_one, char_two = char_select()
    if int(char_one[4]) > int(char_two[4]):
        first = char_one
        second = char_two
    elif int(char_two[4]) > int(char_one[4]):
        first = char_two
        second = char_one
    else:
        if random.randint(1,2) == 1:
            first = char_one
            second = char_two
        else:
            first = char_two
            second = char_one
    while True:
        if turn(first, second):
            exp = int(first[7])/3 + 10
            print(f'{second[0]} won!\nThey have recieved {exp} experience points!')
            if second == char_one:
                return [char_one, exp]
            else:
                return [char_two, exp]
        if turn(second, first):
            exp = int(second[7])/3 + 10
            print(f'{first[0]} won!\nThey have recieved {exp} experience points!')
            if first == char_one:
                return [char_one, exp]
            else:
                return [char_two, exp]