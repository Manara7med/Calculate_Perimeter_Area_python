import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
print("...Circle...")
radius = int(input("enter the radius : "))
            
circle = Circle(radius)
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()
                        
print("Radius of the circle:",radius)
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)

print("*******************************************")
print("... Rectangle...")
length=int(input("enter the length of the rectangle : "))
width=int(input("enter the width of the rectangle : "))

rectangle = Rectangle(length, width)
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()

print("\nRectangle: Length =",length," Width =",width)
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)

print("*******************************************")
print("... Triangle...")
base = int(input("enter the base of the Triangle : "))
height = int(input("enter the height of the Triangle : "))
s1 = int(input("enter the side1 of the Triangle : "))
s2 = int(input("enter the side2 of the Triangle : "))
s3 = int(input("enter the side3 of the Triangle : "))

print("\nTriangle: Base =",base," Height =",height," side1 =",s1," side2 =",s2," side3 =",s3)
triangle = Triangle(base,height,s1,s2,s3)
triangle_area = triangle.calculate_area()
triangle_perimeter = triangle.calculate_perimeter()
print("Triangle Area:", triangle_area)
print("Triangle Perimeter:", triangle_perimeter)



