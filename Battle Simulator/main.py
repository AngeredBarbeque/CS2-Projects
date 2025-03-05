#Allows the user to create a character
def create():
    while True:
        name = input("What is the name of your character?\n")
        print("What class is your character?\n1:Warrior: Boosted defense\nSlam: Hits enemy with a chance to stun.\nAt level 5: Prepare: Further boosts defense for 3 turns.\n")
        print("2:Rogue: Boosted speed\nAmbush: Sneak attacks an enemy to ignore part of their defense.\nAt level 5: Crafty: Has a chance to critical hit on any attack.\n")
        print("3:Brute: Boosted strength\nVicious Strike: Attacks for doubled damage, but always goes last.\nAt level 5: Second Wind: After dropping to 0 health for the first time in a battle, revives with 1 health.\n")
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
    if char_class == 'Warrior':
        defense += 3
    elif char_class == 'Rogue':
        speed += 5
    elif char_class == 'Brute':
        strength += 5
    with open('Battle Simulator/chars.csv', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(name, health, strength, defense, speed)
create()
