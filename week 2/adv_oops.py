import math

class Shape:
    def area(self):
        return NotImplementedError("Sub classes are not initialized")
    
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle with radius {self.radius}"
    
class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def __str__(self):
        return f"Rectangle {self.length} * {self.width}"
    
shapes = [
    Circle(5),
    Rectangle(2,5)
]

for shape in shapes:
    print(f"{shape} -> Area {shape.area()}")
        


#man it was tough, but not too much 