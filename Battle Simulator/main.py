import csv
from character_management import *
import random
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
def main():
    print("Hello! Welcome to your battle simulator! You can use this to create characters for you and your friends, and then have them battle each other!")
    while True:
        choice = inquirer.select(
        message="Select an action:",
        choices=[
            "Create a character",
            "View characters",
            'Battle',
            "Exit",
        ],
        filter = lambda result:result.split()[0].lower(),
        default=None,
    ).execute()
        if choice == 'create':
            create()
        elif choice == 'view':
            display_chars()
        elif choice == 'battle':
            pass
        elif choice == 'exit':
            exit()
        else:
            print('Please enter 1, 2, 3, or 4.')
main()