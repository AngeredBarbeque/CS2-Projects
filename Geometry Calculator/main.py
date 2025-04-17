# Geometry Calculator Nicholas Larsen
from shape_management import *
import InquirerPy as inq
rects = []
tris = []
circs = []
def main():
    print("Hello! This is a 2D geometry calculator!")
    choice = inq.select(
        message = 'What would you like to do?',
        choices = ["Input A New Shape","Compare Existing Shapes","Exit"]
    )
    if choice == 'Input A New Shape':
        shape = inq.select(
            message = 'What kind of shape are you entering?',
            choices = ['Square','Triangle','Circle']
        )
    elif choice == 'Compare Existing Shapes':
        pass
    elif choice == 'Exit':
        exit()