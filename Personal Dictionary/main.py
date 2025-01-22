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
        return
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
                    return
        print("That book doesn't exist.")
        return
    else:
        return

#searches for items within the library
def search(library):
    item = input("\nWhat would you like to search for in your library? You can search using the book's name, genre, author, or page number:")
    if item != 'e':
        #checks each book in library
        for i in library:
            #checks each attribute of the book
            for attribute in i:
                if attribute == item:
                    #prints the attributes of the book and the spot in the list
                    print("\nFound it! The book is", i[0], "by", i[1] +',', i[2], "pages long, and a", i[3], "book.\nIt is item", library.index(i)+1, "in your library.")
                    return
        print("Sorry, I couldn't find that book.")
        return
    else:
        return
#main function that allows the user to choose what they want to do
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