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
                print("Critical strike!")
                damage = int(char[2]) * 3 - int(opponent[3])
            else:
                damage = int(char[2]) - int(opponent[3])
        elif choice == 'Eat Scraps':
            health = round(health*1.2)
            print("You healed youself by eating scraps!")
            damage = 0
        elif choice == 'Lawsuit':
            #ADD FUN MESSAGES
            opponent[8] = True
            damage = 0
        elif choice == 'Reverse Jury Nullification':
            #ADD FUN MESSAGES
            damage = int(char[2]) * 2 - int(opponent[3])
        elif choice == 'Preserve':
            damage = 0
            char[3] = round(int(char[3]) * 1.2)
            print("You preserve yourself, increasing your defense!")
        elif choice == 'Arson':
            damage = char[2]
        if damage < 0:
            damage = 0
        opponent_health = opponent_health - int(damage)
        print(f"Your opponent took {damage} damage!\n")
        if opponent[8]:
            print("Your opponent took 5 damage due to your lawsuit!")
            opponent_health -= 5
        if char[8]:
            print("You took 5 damage due to your opponent's lawsuit!")
            health -= 5
        if opponent_health <= 0:
            opponent_health = 0
            return 'w'
        if health <= 0:
            health = 0
            return 'l'
        char[1] = health
        opponent[1] = opponent_health
        return [char, opponent]
    
    def play_turns(first, char_one, char_two):
        if first == 'one':
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
                    char_two = turn_two[0]
                    char_one = turn_two[1]
                    
        elif first == 'two':
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
                    char_one = turn_one[1]
                    char_two = turn_one[0]

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
                    char_one = turn_two[0]
                    char_two = turn_two[1]


    characters = char_select()
    if characters:
        char_one = characters[0]
        char_two =characters[1]
        char_one.append(False)
        char_two.append(False)

        if int(char_one[4]) > int(char_two[4]):
            [char, exp] = play_turns('one', char_one, char_two)

        elif int(char_one[4]) < int(char_two[4]):
            [char, exp] = play_turns('two', char_one, char_two)

        else:
            num = random.randint(0, 1)
            
            if num == 1:
                [char, exp] = play_turns('one', char_one, char_two)
            else:
                [char, exp] = play_turns('two', char_one, char_two)
        return [char, exp]
    else:
        return False
