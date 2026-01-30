# Python file/script to define a 'circle' class

#import the in-built math module
import math #allows us to access the in-built value of pi and pow() function

class Circle:
    def __init__(self, radius = 0): #creates a circle with a default radius of 0
        self.radius = radius

    def calc_area(self):
        #return math.pi * self.radius ** 2 #same as code below
        return math.pi * math.pow(self.radius, 2)

    def calc_circumference(self):
        return math.pi * (self.radius * 2)

    def __str__(self): #dunder(double underscore) method
        return (f"Circle's Dimensions"
                f"\n"+ "-" * 40 +
                f"Radius: {self.radius} cm."
                f"\nArea: {self.calc_area():.2f} cm^2."
                f"\nCircumference: {self.calc_circumference():.2f} cm."
                f"\n" + "-" * 40)

