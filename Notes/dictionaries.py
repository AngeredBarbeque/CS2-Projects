#Nicholas Larsen, Dictionaries Notes

#What is a dictionary?

"""A dictionary is a list that contains key:value pairs."""

#What are keys?

'''A key is the name associated with values in a dictionary, similar to the name of a variable.'''

#What are values?

'''Values are the values assocated with a key in a dictionary, similar to the value of a varaible.'''

#How do you write a dictionary?

car ={
    'make':'Ford',
    'model':'EscapeXLT',
    'year': 2008,
    'color': 'red',
}

print(car['make'])


#What data types can you have in a dictionary?

'''Any data types are allowed'''

#How do you print 1 item from a dictionary?

print(car['make'])

#Why would you use a dictionary in a program?

"""dictionaries are used if you have a variable with specific information attached to them."""

#What methods can be used with dictionaries?


'''

car.keys()

car.values()

car.pop('color')

car.copy

car.clear

car.get('make)

car.setdefault('color', 'white')

car.update({'year':2025})

'''




avatar = {
    'earth' : {
        'main_char': {
            'toph':'best member of team avatar. invented metal bending',
        },
    },
    'water' : {
        'main_char': {
            'katara':'team water bender. team mom. mastered blood bending',
            'sokka':'team leader. weilds a boomerang and a sword (later)',
        },
    },
    'fire' : {
        'main_char': {
            'zuko':'team lancer. joins in book 3. team firebender. other favorite character.',
        },
    },
    'air' : {
        'main_char': {
            'aang':'Main character. The avatar.team airbender',
        },
    },
}