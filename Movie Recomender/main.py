#Nicholas Larsen Movie Recomender

import csv
movies = []

#opens the csv file containing the movies, and appends a dictionary containing a movie and its details to the main list
def read(movies):
    with open("Movie Recomender\movies.csv", 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for movie in csv_reader:
            movies.append({
                movie[0]:{
                    "Directer":movie[1],
                    "Genre":movie[2],
                    "Rating":movie[3],
                    "Length":movie[4],
                    "Notable Actors":movie[5]
                }
            })
        return movies

#prints the list of movies
def show(movies):
    for i in movies:
        for item in i:
            print(item)
        print(i)

movies = read(movies)
show(movies)
