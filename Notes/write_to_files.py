#How do you find a file in a folder? 

"right click and use the relative path"

#In a python project how do you open a file?


"Text file"

with open ('Notes/things.txt', 'w+') as file:
    file.write("Thing to now be in the file")
    print(file.read())



"CSVs"

import csv

items = [
    ['lactose', 'blue'],
    ['jonas', 'black']
]

with open('Notes\sample.csv', 'w', newline='') as file:
    #fieldnames tells it what rows to skip and not print
    #delimiters tell it something else to split by instead of commas
    csv_writer = csv.writer(file, delimiter='|')
    csv_writer.writerows(items)


with open('Notes\sample.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter='|')
    for row in csv_reader:
        print(f'\nUsername: {row[0]}\nFavorite Color: {row[1]}')



#What is the difference between writing, appending, and creation modes?
"""
r = read only (error is no file exists)
w = write only (error is no file exists)
w+ = read and write (error is no file exists)
a = append (adding but no overwriting) (can create a file if no file exists)
a+ = read and append
x = create a file
"""