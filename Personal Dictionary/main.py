library = []

#adds new items to the library
def add():
    item = input("\nWhat would you like to add to your library?")
    if item != "e":
        #!!FIX THIS!!
        print(library)
        add()
    else:
        return

#removes items from the library
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

#searches for items withing the library
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