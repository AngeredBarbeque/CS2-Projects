#Nicholas Larsen, Reading files notes
import csv
users = {}

#How do you open a file in your program?

with open('Notes/things.txt', 'r') as file:
    content = file.read()
    index = content.find('teeth')
    print(content[index:index+5])

#How do you alter text to work as data in a program?

"The file is imported as a string, at which point you can use it the same way you would use any other string."

#What is a CSV file?

"Comma seperated values, a type of text file with specific properties."

#How are they used in programming?

"CSVs are easier to use than normal .txt files."

with open('Notes\sample.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        users.update({row[0]:row[1]})
print(users)


#worse syntax
file = open('Notes\sample.csv', 'r')
csv_reader = csv.reader(file)