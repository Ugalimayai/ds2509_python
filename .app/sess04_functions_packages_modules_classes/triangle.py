#python script/file to define a triangle class
#import relevant modules

import math

class Triangle:
    """
    A triangle is a polygon with three corners and three sides.
    Attributes
    side a: int/float
    side b: int/float
    side c: int/float

    Methods
    -----------------------
    triangle_area(): float
    returns the area of the triangle
    triangle_perimeter(): float
    returns the perimeter of the triangle
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def triangle_perimeter(self):
        return self.a + self.b + self.c

    def triangle_area(self):
        semiperimeter = (self.a + self.b + self.c) * 0.5
        return math.sqrt(semiperimeter*(semiperimeter-self.a)*(semiperimeter-self.b)*(semiperimeter-self.c))

    def __str__(self):
        return (f"The Dimensions of the Triangle\n"
                f"\n" + "-" * 40 +
                f"\nSides: {self.a},{self.b},{self.c}"
                f"\nPerimeter: {self.triangle_perimeter()}"
                f"\nArea: {self.triangle_area():.2f}"
                f"\n" + "-" * 40)
