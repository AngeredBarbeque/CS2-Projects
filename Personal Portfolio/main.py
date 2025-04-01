# Personal Portfolio Nicholas Larsen
from InquirerPy import inquirer
from  Battle_Simulator.main import *
from Morse_Code_Translater.main import *
from Movie_Recomender.main import *
from Music_Festival.main import *
from To_Do_List.main import *
from  Word_Counter.main import *
def main():
    while True:
        print("Hello! Welcome to my personal portfolio!\nYou can use the up and down arrow keys to navigate most menus!")
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
            while True:
                desc = inquirer.select(
                message='What project would you like to see a description for?',
                choices = [
                    'Battle Simulator',
                    'Morse Code Translator',
                    'Movie Recomender',
                    'Music Festival Planner',
                    'To-Do List',
                    'Word Counter',
                    'None'
                    ],
                    default=None,
                    ).execute()
                if desc == 'Battle Simulator':
                    print("This battle simulator is one of my most complex solo projects at the moment.\n"
                    "It allows a user to select a character from one of three classes,\n"
                    "and then fight other character's they've made, allowing them to level up.\n"
                    "After leveling up enough, they will unlock a new special move per class.")
                elif desc == 'Morse Code Translator':
                    print("This morse code translator was fairly simple to create,\n"
                    "however I am happy that it turned out the way it did.\n"
                    "This program allows you to translate either english to morse code or vice versa.")
                elif desc == 'Movie Recomender':
                    print("This move recomender was really my first time using a .csv file,\n"
                    "and overall one of the first projects I did utilizing multiple files.\n"
                    "This program will allow you to select filters in order to have movies recomended to you from a fairly large list.")
                elif desc == 'Music Festival Planner':
                    print("This program was my first large group project, and I was the team leader.\n"
                    "I found this  project important because it was the first time\n"
                    "I had to manage files through github more than just submitting a website URL.\n"
                    "This program allows you to manage a music festival using things like stage managment or\n"
                    "assigning  time slots.")
                elif desc == 'To-Do List':
                    print("This program is my very first project using multiple files.\n"
                    "It allows you to check and uncheck tasks on a to-do list, along with viewing said tasks.\n"
                    "The tasks are then saved to a text file, thus marking my first time saving data  over multiple runs of the program.")
                elif desc == 'Word Counter':
                    print("This program was one of my first using multiple files in order to arange my functions more effectively.\n"
                    "This program asks for a file directory, and then uses it in order to mark the file with a word count\n"
                    "and a timestamp.")
                else:
                    return
        else:
            print("Goodbye!")
            exit()
main()