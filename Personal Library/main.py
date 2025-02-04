library = []

#adds new items to the library
def add(library):
    book = input("\nWhat is the name of the book would you like to add to your library?")
    if book != "e":
        author = input("\nWho wrote the book?")
        pages = input("\nHow many pages long is the book?")
        genre = input("\nWhat genre is the book?")
        #Creates a dictionary to store the book
        library.append({
            'Name':book,
            'Author':author,
            'Pages':pages,
            'Genre':genre
        })
        show(library)
        return
    else:
        return

#removes items from the library
def rmove(library):
    item = input("\nWhat would you like to remove from your library? You can choose a book with its name, genre, author, or page number:\n")
    if item != "e":
        for i in library:
            for attribute in i:
                if i[attribute] == item:
                    library.remove(i)
                    print("Got it!")
                    return
        print("That book doesn't exist.")
        return
    else:
        return
def edit(library):
    item = input("\nWhat book would you like to change in your library? You can choose a book with its name, genre, author, or page number:\n")
    if item != "e":
        for i in library:
            for attribute in i:
                if i[attribute] == item:
                    choice = input("Would you like to\n1:Edit name\n2:Edit author\n3:Edit page number\n4:Edit genre\nChoose:")
                    if choice == '1':
                        name = input("What would you like to rename the book?\n")
                        i.update({'Name':name})
                        return
                    elif choice == '2':
                        author = input("What would you like the new author to be?\n")
                        i.update({'Author':author})
                        return
                    elif choice == '3':
                        pages = input("What would you like the new page number to be?\n")
                        i.update({'Pages':pages})
                        return
                    elif choice == '4':
                        genre = input("What would you like the new genre to be?\n")
                        i.update({'Genre':genre})
                        return
                    elif choice == 'e':
                        return
                    else:
                        print("Sorry, please enter 1, 2, 3, 4, or e.")
        print("Couldn't find that book.")
        return
    else:
        return

#searches for items within the library
def search(library):
    item = input("\nWhat would you like to search for in your library? You can search using the book's name, genre, author, or page number:\n")
    if item != 'e':
        #checks each book in library
        for i in library:
            #checks each attribute of the book
            for attribute in i:
                if i[attribute] == item:
                    #prints the attributes of the book and the spot in the list
                    print(f"\nFound it! The book is {i['Name']}, by {i['Author']}, {i['Pages']} pages long, and a {i['Genre']} book.")
                    return
        print("Sorry, I couldn't find that book.")
        return
    else:
        return

#A function to print the library in a more appealing way
def show(library):
    for item in library:
        print(f"{item['Name']} by {item['Author']}, a {item['Genre']} book, and {item['Pages']} pages long.")

#Prints some important details about the books, but not everything.
def simple_show(library):
    for item in library:
        print(f'{item['Name']} by {item['Author']}.')

#main function that allows the user to choose what they want to do
def main():
    print("\nHello! Welcome to your perosnal library!\nThis program will help you manage a collection of books.\nIf at any point you want to exit, enter 'e'.\n")
    #loops so that the program runs until the user tells it to stop
    while True:
        choice = input("\nWhat would you like to do?\n1:Add items to your library.\n2:Remove items from your library.\n3:Search for an item in your library.\n4:View full Library\n5:View simple library\n6:Edit a book\nChoose:")
        if choice == '1':
            add(library)
        elif choice == '2':
            rmove(library)
        elif choice == '3':
            search(library)
        elif choice == '4':
            show(library)
        elif choice == 'e':
            print("\nGoodbye!")
            exit()
        elif choice == '5':
            simple_show(library)
        elif choice == '6':
            edit(library)
        else:
            print("\nSorry, didn't get that.")
main()