
from InquirerPy import inquirer as inq
from InquirerPy.validator import EmptyInputValidator as EIV

def sort_area(shapes):
    def key(shape):
        return shape.area
    shapes.sort(reverse=True,key=key)
    return shapes

def sort_perim(shapes):
    def key(shape):
        return shape.perimeter
    shapes.sort(reverse=True,key=key)
    return shapes

def comp_area(shape_one,shape_two):
    if shape_one.area > shape_two.area:
        return shape_one
    elif shape_two.area > shape_one.area:
        return shape_two
    else:
        return 'Tie'

def comp_perim(shape_one,shape_two):
    if shape_one.perimeter > shape_two.perimeter:
        return shape_one
    elif shape_two.perimeter > shape_one.perimeter:
        return shape_two
    else:
        return 'Neither'

def sort_main(rects,tris,circs):
    shapes = rects.copy() + tris.copy() + circs.copy()
    #Runs the secondary choice
    def secondary_choice(shapes):
        choice_two = inq.select(
        message='By what?',
        choices=['Perimeter','Area']
        ).execute()
        if choice_two == 'Perimeter':
            sorted = sort_perim(shapes)
        else:
            sorted = sort_area(shapes)
        return sorted
    
    choice_one = inq.select(
        message = 'What would you like to do?',
        choices = ['Sort rectangles','Sort triangles','Sort circles','Compare shapes','Exit']
    ).execute()

    if choice_one == 'Sort rectangles':
        sorted = secondary_choice(rects)
        for i in sorted:
            print(i)
    elif choice_one == 'Sort triangles':
        sorted = secondary_choice(tris)
        for i in sorted:
            print(i)
    elif choice_one == 'Sort circles':
        sorted = secondary_choice(circs)
        for i in sorted:
            print(i)
    elif choice_one == 'Compare shapes':
        while True:
            shape_one = inq.select(
                message = 'What is the first shape you would like to compare?',
                choices = shapes
            ).execute()
            shape_two = inq.select(
                message = 'What is the second shape you would like to compare?',
                choices = shapes
            ).execute()
            if shape_one == shape_two:
                print("Please select two different shapes.")
                continue
            choice_two = inq.select(
                message = 'Compare by what?',
                choices=['Perimeter','Area']
            ).execute()
            if choice_two == 'Perimeter':
                result = comp_perim(shape_one,shape_two)
            elif choice_two == 'Area':
                result = comp_area(shape_one,shape_two)
            print(f'{result}\nhas a higher {choice_two}')
            break
    else:
        return