from InquirerPy import inquirer as inq

def number_input(message):
    response = input(message+'\n')
    try:
        response = float(response)
        return response
    except:
        print("Please enter a number.")
        number_input(message)

#Creates a class for rectangles
class rect:
    def __init__(self,length,width,perimeter,area):
        self.length = length
        self.width = width
        self.perimeter = perimeter
        self.area = area

    def __str__(self):
        return f'Shape: Rectangle\nLength: {self.length}\nWidth: {self.width}\nPerimeter: {self.perimeter}\nArea: {self.area}'

    def perim_calc(self):
        return round((self.length + self.width) * 2,4)

    def area_calc(self):
        return round(self.length * self.width,4)
    
#Creates a rectangle subclass called square
class square(rect):
    def __init__(self,length,width,area,perimeter):
        super().__init__(length,width,area,perimeter)

    def __str__(self):
        return f'Shape: Rectangle\nLength: {self.length}\nWidth: {self.width}\nPerimeter: {self.perimeter}\nArea: {self.area}'
    
    def area_calc(self):
        return round(self.length * self.length,4)

    def perim_calc(self):
        return round(4*self.length,4)

#Creates a class for triangles
class tri:
    def __init__(self,height,side_one,side_two,side_three,perimeter,area):
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three
        self.height = height
        self.perimeter = perimeter
        self.area = area

    def __str__(self):
        return f'Shape: Triangle\nSide Lengths: {self.side_one}, {self.side_two}, {self.side_three}\nHeight: {self.height}\nPerimeter: {self.perimeter}\nArea: {self.area}'

    def perim_calc(self):
        return round(self.side_one + self.side_two + self.side_three,4)

    def area_calc(self):
        return round(self.side_one * self.height,4)

#Creates a class for circles
class circl:
    def __init__(self,radius,perimeter,area):
        self.radius = radius
        self.perimeter = perimeter
        self.area = area

    def __str__(self):
        return f'Shape: Circle\nRadius: {self.radius}\nCircumfrence: {self.perimeter}\nArea: {self.area}'

    def perim_calc(self):
        return round((self.radius*2)*3.141592,4)

    def area_calc(self):
        return round((self.radius * self.radius)*3.141592,4)
            
#Creates a rectangle
def make_rect():
    length = number_input('How long is the rectangle?')
    width = number_input('How wide is the rectangle?')
    if width == length:
        rectangle = square(length,width,0,0)
    else:
        rectangle = rect(length,width,0,0)
    rectangle.perimeter = rectangle.perim_calc()
    rectangle.area = rectangle.area_calc()
    print(rectangle)
    return rectangle

#Creates a triangle
def make_tri():
    side_one = number_input('What is the length of the base of the triangle?')
    side_two = number_input('What is the length of another side of the triangle?')
    side_three = number_input('What is the length of the final side of the triangle?')
    height = number_input('What is the height of the triangle?')
    triangle = tri(height,side_one,side_two,side_three,0,0)
    triangle.area = triangle.area_calc()
    triangle.perimeter = triangle.perim_calc()
    print(triangle)
    return triangle

#Creates a circle
def make_circle():
    rad = number_input('What is the radius of the circle?')
    circle = circl(rad,0,0)
    circle.area = circle.area_calc()
    circle.perimeter = circle.perim_calc()
    print(circle)
    return circle
