import csv
from battle_management import *
from character_management import *
import random
from InquirerPy import inquirer

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
        elif choice == 'Exit':
            exit()
main()
