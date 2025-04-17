from main import rects
from main import tris
from main import circs
import InquirerPy as inq
from InquirerPy.validator import EmptyInputValidator as EIV
def def_classes():
    class rect:
        def __init__(self,length,width,perimeter,area):
            self.length = length
            self.width = width
            self.perimeter = perimeter
            self.area = area
        def perim_calc(self):
            self.perimeter = (self.length + self.width) * 2
        def area_calc(self):
            self.area = self.length * self.width

    class tri:
        def __init__(self,height,side_one,side_two,side_three,perimeter,area):
            self.side_one = side_one
            self.side_two = side_two
            self.side_three = side_three
            self.height = height
            self.perimeter = perimeter
            self.area = area
        def perim_calc(self):
            self.perimeter = self.side_one + self.side_two + self.side_three
        def area_calc(self):
            self.area = self.side_one * self.height

    class circle:
        def __init__(self,radius,circ,area):
            self.radius = radius
            self.circ = circ
            self.area = area
        def circ_calc(self):
            self.circ = round((self.radius*2)*3.141592,2)
        def area_calc(self):
            self.area = round((self.radius * self.radius)*3.141592,2)
            
def make_rect():
    length = inq.number(
        message = 'How long is the rectangle?',
        validate = EIV
    )
    width = inq.number(
        message = 'How wide is the rectangle?',
        validate = EIV
    )
    #MAKE SQUARES AND STUFF
def make_tri():
    side_one = inq.number(
        message = 'What is the base of the triangle?',
        validate = EIV
    )
def make_circle():
    pass
