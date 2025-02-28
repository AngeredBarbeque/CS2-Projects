#Nicholas Larsen, Multiple pages and importing files


#How do you make multiple files in python?

'Create a folder containing multiple files.'

#How do you get a function from another file

from calcs import add as beef_stew
print(beef_stew(2,3))

#How do you get variables from another file?

'Import a function containing the nessecary variable values'

#How do you have a function with multiple returns?

def info():
    return "Jonas", '32', 'Neon purple'

name, age, color = info()

#Why would you use multiple pages for a python project?

'To reduce the amount of merge conflicts, and make things cleaner and easier to read.'