# Geometry Calculator Nicholas Larsen
from shape_management import *
from InquirerPy import inquirer as inq
rects = []
tris = []
circs = []
def main():
    print("Hello! This is a 2D geometry calculator!")
    while True:
        choice = inq.select(
            message = 'What would you like to do?',
            choices = ["Input A New Shape","Compare Existing Shapes","Exit"]
        ).execute()
        if choice == 'Input A New Shape':
            shape = inq.select(
                message = 'What kind of shape are you entering?',
                choices = ['Rectangle','Triangle','Circle']
            ).execute()
            if shape == 'Rectangle':
                rects.append(make_rect())
            elif shape == 'Triangle':
                tris.append(make_tri())
            elif shape == 'Circle':
                circs.append(make_circle())
        elif choice == 'Compare Existing Shapes':
            pass
        elif choice == 'Exit':
            exit()
main()