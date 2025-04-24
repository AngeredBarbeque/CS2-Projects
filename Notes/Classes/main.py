# Classes and Objects Notes

#What is a class in python?

    # A class is a blueprint for creating objects

#How do you create a python class?
class pokemon:
    def __init__(self, name, species, attack, hp):
        self.name = name
        self.species = species
        self.hp = hp
        self.attack = attack

    def __str__(self):
        return f'{self.name}:\nA {self.species} with {self.hp} hit points, and {self.attack} attack.'

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.attack
            print(f'{self.name} attacked {opponent.name} for {self.attack} leaving them with {opponent.hp} hp.')
            if opponent.hp > 0:
                self.hp -= opponent.attack
                print(f'{opponent.name} attacked {self.name} for {opponent.attack} leaving them with {self.hp} hp.')
                if self.hp <= 0:
                    print(f'{self.name} is lying dead on the floor. {opponent.name} looks horrified at their actions.')
            else:
                print(f'{opponent.name} is lying dead on the floor. {self.name} looks horrified at their actions.')


#How do you create a python object?
dracula = pokemon("Mr. Dracula","Charizard",32,10000)
salad = pokemon('Mrs. Dracula',"Bulbasaur",10000,32)
print(dracula)

#How to you call a method for an object?
dracula.battle(salad)

#What is an object in python?

    #An instance of a class.

#How do python classes relate to python objects?

    # They are used to create objects.

#What are methods?

    # A function specific to a class.

#Why do we use python classes?

    #It allows us to organize our information, and simplifies later code.