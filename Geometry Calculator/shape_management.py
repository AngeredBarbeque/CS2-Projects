from InquirerPy import inquirer as inq
from InquirerPy.validator import EmptyInputValidator as EIV

class rect:
    def __init__(self,length,width,perimeter,area):
        self.length = int(length)
        self.width = int(width)
        self.perimeter = perimeter
        self.area = area

    def __str__(self):
        return f'Shape: Rectangle\nLength: {self.length}\nWidth: {self.width}\nPerimeter: {self.perimeter}\nArea: {self.area}'

    def perim_calc(self):
        return (self.length + self.width) * 2

    def area_calc(self):
        return self.length * self.width

class square(rect):
    def __init__(self,length,width,area,perimeter):
        super().__init__(length,width,area,perimeter)

    def __str__(self):
        return f'Shape: Rectangle\nLength: {self.length}\nWidth: {self.width}\nPerimeter: {self.perimeter}\nArea: {self.area}'
    
    def area_calc(self):
        return self.length * self.length

    def perim_calc(self):
        return 4*self.length

class tri:
    def __init__(self,height,side_one,side_two,side_three,perimeter,area):
        self.side_one = int(side_one)
        self.side_two = int(side_two)
        self.side_three = int(side_three)
        self.height = int(height)
        self.perimeter = perimeter
        self.area = area

    def __str__(self):
        return f'Shape: Triangle\nSide Lengths: {self.side_one}, {self.side_two}, {self.side_three}\nHeight: {self.height}\nPerimeter: {self.perimeter}\nArea: {self.area}'

    def perim_calc(self):
        return self.side_one + self.side_two + self.side_three

    def area_calc(self):
        return self.side_one * self.height

class circl:
    def __init__(self,radius,circ,area):
        self.radius = int(radius)
        self.circ = circ
        self.area = area

    def __str__(self):
        return f'Shape: Circle\nRadius: {self.radius}\nCircumfrence: {self.circ}\nArea: {self.area}'

    def circ_calc(self):
        return round((self.radius*2)*3.141592,2)

    def area_calc(self):
        return round((self.radius * self.radius)*3.141592,2)
            

def make_rect():
    length = inq.number(
        message = 'How long is the rectangle?',
        validate = EIV()
    ).execute()
    width = inq.number(
        message = 'How wide is the rectangle?',
        validate = EIV()
    ).execute()
    if width == length:
        rectangle = square(length,width,0,0)
    else:
        rectangle = rect(length,width,0,0)
    rectangle.perimeter = rectangle.perim_calc()
    rectangle.area = rectangle.area_calc()
    print(rectangle)
    return rectangle


def make_tri():
    side_one = inq.number(
        message = 'What is the length of the base of the triangle?',
        validate = EIV()
    ).execute()
    side_two = inq.number(
        message = 'What is the length of another side of the triangle?',
        validate = EIV()
    ).execute()
    side_three = inq.number(
        message = 'What is the length of the final side of the triangle?',
        validate = EIV()
    ).execute()
    height =  inq.number(
        message = 'What is the height of the triangle?',
        validate  = EIV()
    ).execute()
    triangle = tri(height,side_one,side_two,side_three,0,0)
    triangle.area = triangle.area_calc()
    triangle.perimeter = triangle.perim_calc()
    print(triangle)
    return triangle


def make_circle():
    rad = inq.number(
        message = 'What is the radius of the circle?',
        validate = EIV()
    ).execute()
    circle = circl(rad,0,0)
    circle.area = circle.area_calc()
    circle.circ = circle.circ_calc()
    print(circle)
    return circle
