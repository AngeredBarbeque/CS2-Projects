from character_management import *
import random
#Runs a battle, eventually returning the exp gain of the character that won
def battle():
    def turn(char, oppenent):
        health = char[1]
        oppenent_health = oppenent[1]
        #Gives the player their abilities
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
        elif choice == 'Headbutt':
            if random.randint(1, 5) == 5:
                damage = char[2] * 1.5 - oppenent[3]
            else:
                damage = char[2] - oppenent[3]
        elif choice == 'Eat Scraps':
            health += health * 0.2
        elif choice == 'Lawsuit':
            oppenent[8] = True
        elif choice == 'Reverse Jury Nullification':
            damage = char[2] + 10 - oppenent[3]
        elif choice == 'Preserve':
            char[2] *= 1.2
        elif choice == 'Arson':
            damage = char[2]
        oppenent_health -= damage
        if oppenent[8]:
            oppenent_health - 5
            #ADD LAST OF END OF TURN STUFF

    char_one, char_two = char_select()
    char_one.append(False)
    char_two.append(False)
    char_one.append(False)
    char_two.append(False)
    if int(char_one[4]) > int(char_two[4]):
        while True:
            if turn(char_one, char_two) == 'w':
                exp = int(char_two[6]) * 20
                print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                return [char_one, exp]
            
            if turn(char_two, char_one) == 'w':
                exp = int(char_one[6]) * 20
                print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                return [char_two, exp]
    elif int(char_one[4]) < int(char_two[4]):
        while True:

            if turn(char_two, char_one) == 'w':
                exp = int(char_one[6]) * 20
                print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                return [char_two, exp]
            
            if turn(char_one, char_two) == 'w':
                exp = int(char_two[6]) * 20
                print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                return [char_one, exp]
    else:
        num = random.randint(0, 1)
        if num == 1:
            while True:

                if turn(char_one, char_two) == 'w':
                    exp = int(char_two[6]) * 20
                    print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_one, exp]
                
                if turn(char_two, char_one) == 'w':
                    exp = int(char_one[6]) * 20
                    print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_two, exp]
                
        else:
            while True:
                if turn(char_two, char_one) == 'w':
                    exp = int(char_one[6]) * 20
                    print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_two, exp]
                
                if turn(char_one, char_two) == 'w':
                    exp = int(char_two[6]) * 20
                    print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_one, exp]