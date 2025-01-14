#creates empty list to store items later
library = []

def add():
    item = input("\nWhat would you like to add to your library?")
    if item != "e":
        library.append(item)
        print(library)
        add()
    else:
        return
def rmove():
    item = input("\nWhat would you like to remove from your library?")
    if item != "e":
        try:
            library.remove(item)
            print(library)
        except:
            print("\nSorry, that didn't work.")
        rmove()
    else:
        return
def search():
    item = input("\nWhat would you like to search for in your library?")
    if item != 'e':
        if item in library:
            print("\nFound it! It's item", (library.index(item)+1), "in your library!")
        else:
            print("\nSorry, that doesn't seem to be in your library.")
    else:
        return
def main():
    #Welcomes and explains to the user what this project does
    print("\nHello! Welcome to your perosnal library!\nThis program will help you manage a collection of books.\nIf at any point you want to exit, enter 'e'.\n")
    while True:
        choice = input("\nWhat would you like to do?\n1:Add items to your library.\n2:Remove items from your library.\n3:Search for an item in your library.\nChoose:")
        if choice == '1':
            add()
        elif choice == '2':
            rmove()
        elif choice == '3':
            search()
        elif choice == 'e':
            print("\nGoodbye!")
            exit()
        else:
            print("\nSorry, didn't get that.")
main()