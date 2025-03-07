from character_management import *
import random
#Runs a battle, eventually returning the exp gain of the character that won
def battle():
    def turn(char, opponent):
        print(f"{char[0]}'s turn!")
        health = int(char[1])
        opponent_health = int(opponent[1])
        print(f"{opponent[0]}'s health:\n{opponent_health}")
        print(f'Your health is:\n{health}')
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
        options = ['Normal Strike']
        for i in abilities:
            options.append(i)
        choice = inquirer.select(
            message="Select an action:",
            choices=options,
            default=None,
            ).execute()
        if choice == 'Normal Strike':
            damage = int(char[2]) - int(opponent[3])
        elif choice == 'Headbutt':
            if random.randint(1, 5) == 5:
                damage = int(char[2]) * 1.5 - int(opponent[3])
            else:
                damage = int(char[2]) - int(opponent[3])
        elif choice == 'Eat Scraps':
            health *= 1.2
        elif choice == 'Lawsuit':
            opponent[8] = True
            damage = 0
        elif choice == 'Reverse Jury Nullification':
            damage = int(char[2]) * 2 - int(opponent[3])
        elif choice == 'Preserve':
            char[2] *= 1.2
        elif choice == 'Arson':
            damage = char[2]
        opponent_health -= damage
        if opponent[8]:
            opponent_health - 5
        if char[8]:
            health - 5
        if opponent_health <= 0:
            opponent_health = 0
            return 'w'
        if health <= 0:
            health = 0
            return 'l'
        return [char, opponent]

    characters = char_select()
    char_one = characters[0]
    char_two =characters[1]
    char_one.append(False)
    char_two.append(False)
    print(char_one)
    print(char_two)
    if int(char_one[4]) > int(char_two[4]):
        while True:

            turn_one = turn(char_one, char_two)
            if turn_one == 'w':
                exp = int(char_two[6]) * 20
                print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                return [char_one, exp]
            
            elif turn_one == 'l':
                exp = int(char_one[6]) * 20
                print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                return [char_two, exp]
            
            else:
                char_one = turn_one[0]
                char_two = turn_one[1]

            turn_two = turn(char_two, char_one)
            if turn_two == 'w':
                exp = int(char_one[6]) * 20
                print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                return [char_two, exp]
            elif turn_two == 'l':
                exp = int(char_two[6]) * 20
                print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                return [char_one, exp]
            
            else:
                char_two = turn_one[0]
                char_one = turn_one[1]

    elif int(char_one[4]) < int(char_two[4]):
        while True:

            turn_one = turn(char_two, char_one)
            if turn_one == 'w':
                exp = int(char_one[6]) * 20
                print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                return [char_two, exp]
            
            elif turn_one == 'l':
                exp = int(char_two[6]) * 20
                print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                return [char_one, exp]

            else:
                char_one = turn_one[0]
                char_two = turn_one[1]

            turn_two = turn(char_one, char_two)
            if turn_two == 'w':
                exp = int(char_two[6]) * 20
                print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                return [char_one, exp]
            
            elif turn_two== 'l':
                exp = int(char_one[6]) * 20
                print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                return [char_two, exp]
            
            else:
                char_one = turn_one[0]
                char_two = turn_one[1]

    else:
        num = random.randint(0, 1)
        if num == 1:
            while True:

                turn_one = turn(char_one, char_two)
                if turn_one == 'w':
                    exp = int(char_two[6]) * 20
                    print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_one, exp]
                
                elif turn_one == 'l':
                    exp = int(char_one[6]) * 20
                    print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_two, exp]
                
                else:
                    char_one = turn_one[0]
                    char_two = turn_one[1]

                turn_two = turn(char_two, char_one)
                if turn_two == 'w':
                    exp = int(char_one[6]) * 20
                    print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_two, exp]
                elif turn_two == 'l':
                    exp = int(char_two[6]) * 20
                    print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_one, exp]
                
                else:
                    char_one = turn_one[0]
                    char_two = turn_one[1]
                
        else:
            while True:

                turn_one = turn(char_two, char_one)
                if turn_one == 'w':
                    exp = int(char_one[6]) * 20
                    print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_two, exp]
                
                elif turn_one == 'l':
                    exp = int(char_two[6]) * 20
                    print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_one, exp]

                turn_two = turn(char_one, char_two)
                if turn_two == 'w':
                    exp = int(char_two[6]) * 20
                    print(f'{char_one[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_one, exp]
                
                elif turn_two== 'l':
                    exp = int(char_one[6]) * 20
                    print(f'{char_two[0]} won!\nThey have recieved {exp} experience points!')
                    return [char_two, exp]