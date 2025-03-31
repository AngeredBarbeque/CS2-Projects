from character_management import *
import random
from faker import Faker
from faker.providers import DynamicProvider
#Creates a list that faker can use to generate a random animal from that list
animals_provider = DynamicProvider(
    provider_name='animal',
    elements=['manatees', 'squirrels', 'elephants', 'rats', 'dingos', 'John Smith', 'blobfishes', 'ewoks', 'venus flytraps', 'dogs', 'cats']
)
fake = Faker()
fake.add_provider(animals_provider)
#Runs a battle, eventually returning the exp gain of the character that won
def battle():
    def turn(char, opponent):
        print(f"{char['Name']}'s turn!")
        health = int(char['Health'])
        opponent_health = int(opponent['Health'])
        print(f"{opponent['Name']}'s health:\n{opponent_health}")
        print(f'Your health is:\n{health}')
        #Gives the player their abilities
        if char['Class'] == 'Pig':
            abilities = ['Headbutt']
            if int(char['Level']) >= 5:
                abilities.append('Eat Scraps')
        elif char['Class'] == 'Lawyer':
            abilities = ['Lawsuit']
            if int(char['Level']) >= 5:
                abilities.append('Reverse Jury Nullification')
        elif char['Class'] == 'Mummified Dog':
            abilities = ['Preserve']
            if int(char['Level']) >= 5:
                abilities.append('Arson')
        options = ['Normal Strike']
        for i in abilities:
            options.append(i)
        choice = inquirer.select(
            message="Select an action:",
            choices=options,
            default=None,
            ).execute()
        #Checks what the player does and then sets damage accordingly, and activates special effects.
        if choice == 'Normal Strike':
            damage = int(char['Attack']) - int(opponent['Defense'])
        elif choice == 'Headbutt':
            if random.randint(1, 5) == 5:
                print("Critical strike!")
                damage = int(char['Attack']) * 3 - int(opponent['Defense'])
            else:
                damage = int(char['Attack']) - int(opponent['Defense'])
        elif choice == 'Eat Scraps':
            health = round(health*1.2)
            print("You healed youself by eating scraps!")
            damage = 0
        elif choice == 'Lawsuit':
            #Chooses a reason to sue your opponent
            message_num = random.randint(1, 5)
            if message_num == 1:
                message = 'failing to build their snowman wth proper supports!'
            elif message_num == 2:
                message = 'overly sharp archways in their shed!'
            elif message_num == 3:
                message = 'leaving garbonzo beans littered on the floor of the white house!'
            elif message_num == 4:
                message = 'egging the house of celebrity Dwayne "The Rock" Johnson!'
            elif message_num == 5:
                message = 'using radioactive canisters to cook food for customers!'
            print(f"You sued your opponent for {message}\n")
            #Uses char[8] to set status effect to true
            opponent['Lawsuit'] = True
            damage = 0
        elif choice == 'Reverse Jury Nullification':
            message_num = random.randint(1, 5)
            #Chooses a reason to convict your opponent
            if message_num == 1:
                animal = fake.animal()
                message = f'feeding the {animal} next to an obvious "Dont Feed The {animal.title()}" sign.'
            elif message_num == 2:
                message = 'the murder of a 23 year old man named Terrence Smith.'
            elif message_num == 3:
                message = 'stealing milk from the cartons in grocery carts.'
            elif message_num == 4:
                name = fake.first_name()
                animal = fake.animal()
                message = f'illegal ownership of a {animal} named {name}.'
            elif message_num == 5:
                message = 'loitering.'
            print(f"You falsely convicted your opponent of {message}\n")
            damage = int(char['Attack']) * 2 - int(opponent['Defense'])
        elif choice == 'Preserve':
            damage = 0
            char['Defense'] = round(int(char['Defense']) * 1.2)
            print("You preserve yourself, increasing your defense!\n")
        elif choice == 'Arson':
            damage = int(char['Attack'])
        if damage < 0:
            damage = 0
        #Deals damage to your opponent, and applies lawsuit damage.
        opponent_health = opponent_health - int(damage)
        print(f"Your opponent took {damage} damage!\n")
        if opponent['Lawsuit']:
            print("Your opponent took 5 damage due to your lawsuit!\n")
            opponent_health -= 5
        if char['Lawsuit']:
            print("You took 5 damage due to your opponent's lawsuit!\n")
            health -= 5
        if opponent_health <= 0:
            opponent_health = 0
            return 'w'
        if health <= 0:
            health = 0
            return 'l'
        char['Health'] = health
        opponent['Health'] = opponent_health
        return [char, opponent]
    
    def play_turns(first, char_one, char_two):
        if first == 'one':
            while True:
                #Plays a turn, and if someone won, print a message and return the needed information
                turn_one = turn(char_one, char_two)
                if turn_one == 'w':
                    exp = int(char_two['Level']) * 20
                    print(f'{char_one['Name']} won!\nThey have recieved {exp} experience points!')
                    return [char_one, exp]
                
                elif turn_one == 'l':
                    exp = int(char_one['Level']) * 20
                    print(f'{char_two['Name']} won!\nThey have recieved {exp} experience points!')
                    return [char_two, exp]
                
                else:
                    char_one = turn_one[0]
                    char_two = turn_one[1]

                turn_two = turn(char_two, char_one)
                if turn_two == 'w':
                    exp = int(char_one['Level']) * 20
                    print(f'{char_two['Name']} won!\nThey have recieved {exp} experience points!')
                    return [char_two, exp]
                elif turn_two == 'l':
                    exp = int(char_two['Level']) * 20
                    print(f'{char_one['Name']} won!\nThey have recieved {exp} experience points!')
                    return [char_one, exp]
                
                else:
                    char_two = turn_two[0]
                    char_one = turn_two[1]
                    
        elif first == 'two':
            while True:
                turn_one = turn(char_two, char_one)
                if turn_one == 'w':
                    exp = int(char_one['Level']) * 20
                    print(f'{char_two['Name']} won!\nThey have recieved {exp} experience points!')
                    return [char_two, exp]
                
                elif turn_one == 'l':
                    exp = int(char_two['Level']) * 20
                    print(f'{char_one['Name']} won!\nThey have recieved {exp} experience points!')
                    return [char_one, exp]

                else:
                    char_one = turn_one[1]
                    char_two = turn_one[0]

                turn_two = turn(char_one, char_two)
                if turn_two == 'w':
                    exp = int(char_two['Level']) * 20
                    print(f'{char_one['Name']} won!\nThey have recieved {exp} experience points!')
                    return [char_one, exp]
                
                elif turn_two== 'l':
                    exp = int(char_one['Level']) * 20
                    print(f'{char_two['Name']} won!\nThey have recieved {exp} experience points!')
                    return [char_two, exp]
                
                else:
                    char_one = turn_two[0]
                    char_two = turn_two[1]

    #Uses char_select to let the user choose two characters, then appendds false to the eighth index which acts as an indicator for if they've been sued
    characters = char_select()
    #Ensures characters were selected properly.
    if characters:
        char_one = characters[0]
        char_two = characters[1]
        #Chooses what order to play in
        if int(char_one['Speed']) > int(char_two['Speed']):
            [char, exp] = play_turns('one', char_one, char_two)

        elif int(char_one['Speed']) < int(char_two['Speed']):
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
