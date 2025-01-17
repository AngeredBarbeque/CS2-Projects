library = []

#adds new items to the library
def add(library):
    book = input("\nWhat is the name of the book would you like to add to your library?")
    if book != "e":
        author = input("\nWho wrote the book?")
        pages = input("\nHow many pages long is the book?")
        genre = input("\nWhat genre is the book?")
        library.append((book, author, pages, genre))
        print(library)
        add(library)
    else:
        return

#removes items from the library
def rmove(library):
    item = input("\nWhat would you like to remove from your library?")
    if item != "e":
        for i in library:
            for attribute in i:
                if attribute == item:
                    library.remove(i)
                    print("Got it!")
                    rmove(library)
        print("That book doesn't exist.")
        rmove(library)
    else:
        return

#searches for items within the library
def search(library):
    item = input("\nWhat would you like to search for in your library?(Title, length, author, or genre)")
    if item != 'e':
        for i in library:
            for attribute in i:
                if attribute == item:
                    print("\nFound it! The book is", i[0], "by", i[1] +',', i[2], "pages long, and a", i[3], "book.\nIt is item", library.index(i)+1, "in your library.")
                    search(library)
        print("Sorry, I couldn't find that book.")
        search(library)
    else:
        return

def main():
    print("\nHello! Welcome to your perosnal library!\nThis program will help you manage a collection of books.\nIf at any point you want to exit, enter 'e'.\n")
    while True:
        choice = input("\nWhat would you like to do?\n1:Add items to your library.\n2:Remove items from your library.\n3:Search for an item in your library.\n4:View Library\nChoose:")
        if choice == '1':
            add(library)
        elif choice == '2':
            rmove(library)
        elif choice == '3':
            search(library)
        elif choice == '4':
            print(library)
        elif choice == 'e':
            print("\nGoodbye!")
            exit()
        else:
            print("\nSorry, didn't get that.")
main()