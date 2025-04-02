# Personal Portfolio Nicholas Larsen
from InquirerPy import inquirer
from  Battle_Simulator.main import *
from Morse_Code_Translater.main import *
from Movie_Recomender.main import *
from Music_Festival.main import *
from To_Do_List.main import *
from  Word_Counter.main import *
from descriptions import desc

#Allows the user to access projects, along with giving them instructions on how to navigate the menus.
def main():
    print("Hello! Welcome to my personal portfolio!\nThis contains some of the programming projects I've made that I'm most proud of, for one reason or another."
        "\nIf the menu has a ? in front of the question, it can be navigated using the aroow keys.\nOtherwise, type an input in the terminal and then press enter/return.")
    while True:
        #Adds a new line divider bewteen the selection menu and the previous thing.
        print('')
        choice = inquirer.select(
                message="What would you like to do?",
                choices=[
                    "Use Battle Simulator",
                    "Use Morse Code Translator",
                    "Use Movie Recomender",
                    "Use Music Festival Planner",
                    "Use To-Do List",
                    "Use Word Counter",
                    "View Project Descriptions",
                    "Exit",
                ],
                default=None,
                ).execute()
        #Adds a divider between the selection menu and what happens next
        print('')
        if choice == 'Use Battle Simulator':
            battle_main()
        elif choice == 'Use Morse Code Translator':
            morse_main()
        elif choice == 'Use Movie Recomender':
            movie_main()
        elif choice == 'Use Music Festival Planner':
            music_main()
        elif choice == 'Use To-Do List':
            to_do_main()
        elif choice == 'Use Word Counter':
            counter_main()
        elif choice == 'View Project Descriptions':
            desc()
        else:
            print("Goodbye!")
            exit()
main()