#Nicholas Larsen Movie Recomender

import csv

#opens the csv file containing the movies, and appends a dictionary containing a movie and its details to the main list
def read(movies):
    with open("Movie Recomender/movies.csv", 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for movie in csv_reader:
            movies.append({
                #Creates a dictionary with the name of the movie as a key, and the rest of the attributes inside the value, which is set as a dictionary.
                movie[0]:{
                    "Director":movie[1],
                    "Genre":movie[2],
                    "Rating":movie[3],
                    "Length":movie[4],
                    "Notable Actors": movie[5]
                }
            })
        return movies

#prints the list of movies
def show(movies):
    for i in movies:
        for item in i:
            print(item)
            for prop in i[item]:
                print(f'{prop}: {i[item][prop]}')

#adds a filter to the list of filters
def add_filter(filters):
    what = input("Would you like to search by\n1:Movie Title\n2:Director\n3:Genre\n4:Rating\n5:Length\n6:Actor\n")

    if what == '1':
        attribute = input("What title would you like to filter by?\n")
        filters.append(['title', attribute])

    elif what == '2':
        attribute = input("What director would you like to filter by?\n")
        filters.append(['director', attribute])

    elif what == '3':
        attribute = input("What genre would you like to filter by?\n")
        filters.append(['genre', attribute])

    elif what == '4':
        attribute = input("What rating would you like to filter by?\n")
        filters.append(['rating', attribute])

    elif what == '5':
        attribute = input("What length would you like to filter by?\n")
        filters.append(['length', attribute])

    elif what == '6':
        attribute = input("What actor would you like to filter by?\n")
        filters.append(['actor', attribute])
    
    return filters

#a function that removes a filter
def remove_filter(filters):
    while True:
        print("You are filtering by:")
        for i in filters:
            print(i[1])
        choice = input("What would you like to remove? Use 'e' to leave.\n")
        if choice == 'e':
            return filters
        else:
            for i in filters:
                if i[1] == choice:
                    filters.remove(i)

#A function allowing the user to use the list of filters to decide which movies will be shown.
def apply_filters(movies, filters):
    applicable = movies
    #Loops through all the movies, and if they don't fit the filters, removes them from a list of applicable.
    if filters:
        for filter in filters:
            for i in applicable:
                for movie in i:
                    if filters[filters.index(filter)][0] == 'title':
                        if not filters[filters.index(filter)][1] == movie:
                            applicable.remove(i)

                    elif filters[filters.index(filter)][0] == 'director':
                        if not filters[filters.index(filter)][1] == i[movie]["Director"]:
                            applicable.remove(i)

                    elif filters[filters.index(filter)][0] == 'genre':
                        if not filters[filters.index(filter)][1] == i[movie]["Genre"]:
                            applicable.remove(i)

                    elif filters[filters.index(filter)][0] == 'rating':
                        if not filters[filters.index(filter)][1] == i[movie]["Rating"]:
                            applicable.remove(i)

                    elif filters[filters.index(filter)][0] == 'length':
                        if not filters[filters.index(filter)][1] == i[movie]["Length"]:
                            applicable.remove(i)

                    elif filters[filters.index(filter)][0] == 'actor':
                            if not filters[filters.index(filter)][1] in i[movie]["Notable Actors"].split(', '):
                                applicable.remove(i)

        if applicable:
            show(applicable)

        else:
            print("No movies fit your filters.\n")

    else:
        print("You have no filters.")


#A function that allows the user to access the other filtering functions, such as adding and removing
def search(movies, filters):
    while True:
        choice = input("Would you like to\n1:Add a filter\n2:Remove a filter\n3:View aplicable movies\n4:Leave\n")
        if choice == '1':
            filters = add_filter(filters)
        elif choice == '2':
            filters = remove_filter(filters)
        elif choice == '3':
            apply_filters(movies, filters)
        elif choice == '4':
            return filters
        else:
            print("Please enter 1, 2, 3, or 4.\n")

#a function allowing the user to view the list, use filters, or leave.
def main():
    movies = []
    filters = []
    movies = read(movies)
    print("Hello! Welcome to your movie recomender!")
    while True:
        choice = input("Would you like to\n1:View your full list of movies\n2:Search for a specific movie, directer, genre, rating, length, or actors\n3:Leave\n")
        if choice == '1':
            show(movies)
        elif choice == '2':
            filters = search(movies, filters)
        elif choice == '3':
            print("Goodbye!")
            exit()
        else:
            print("Sorry, didn't get that.\n")
            continue

main()