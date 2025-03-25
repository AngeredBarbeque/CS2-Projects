#Imports needed libraries
import csv
from battle_management import *
from character_management import *
import random
from InquirerPy import inquirer

#Uses inquirer py to allow the user to select an option
def main():
    print("Hello! Welcome to your battle simulator! You can use this to create characters for you and your friends, and then have them battle each other!")
    while True:
        choice = inquirer.select(
        message="Select an action:",
        choices=[
            "Create a character",
            "View characters",
            'Battle',
            'Remove a character',
            'View character stat charts',
            'Generate random backstories',
            'View overall character stats',
            "Exit",
        ],
        default=None,
    ).execute()
        if choice == 'Create a character':
            create()
        elif choice == 'View characters':
            display_chars()
        elif choice == 'Battle':
            result = battle()
            if not result:
                continue
            char = result[0]
            exp_gain = result[1]
            edit_char(char, exp_gain)
        elif choice == 'Remove a character':
            remove()
        elif choice == 'View character stat charts':
            display_stat_bars()
        elif choice == 'Generate random backstories':
            backstory, char = backstories()
            char['Backstory'] = backstory
            #SYNC UP WITH OVERALL
        elif choice == 'View overall character stats':
            stat_displays()
        elif choice == 'Exit':
            exit()
main()
