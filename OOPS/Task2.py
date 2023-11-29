import math
from abc import ABC, abstractmethod
class Shape(ABC):
    
    @abstractmethod
    def area(self) :
        pass
    
    @abstractmethod
    def perimeter(self):
        pass   
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length+ self.width)
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
circle = Circle(8)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

rectangle = Rectangle(15, 20)
print("\nRectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

triangle = Triangle(6, 9, 8)
print("\nTriangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())