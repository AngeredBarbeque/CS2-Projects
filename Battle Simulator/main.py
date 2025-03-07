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
        default=None,
    ).execute()
        if choice == 'Create a character':
            create()
        elif choice == 'View characters':
            display_chars()
        elif choice == 'Battle':
            pass
        elif choice == 'Exit':
            exit()
main()