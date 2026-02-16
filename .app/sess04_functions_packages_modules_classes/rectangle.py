# Python file/script to define a rectangle class
#import relevant modules
import math

class Rectangle:
    """
    A class to represent a 2-D rectangle.
    Attributes:
    -----------------------------------
    length/height: float
    width: float

    Methods:
    ------------------------------------
    rect_area():
        Calculates and returns the area of the rectangle.
    rect_perimeter():
        Calculates and returns the perimeter of the rectangle.
    rect_diagonal:
        Calculates and returns the length of the diagonal of the rectangle.
    __str__():
        Returns the string representation of the rectangle's dimensions
    """
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def rect_area(self):
        # returns the area of the rectangle
        return self.width * self.height

    def rect_perimeter(self):
        #returns the perimeter of the rectangle
        return 2 * (self.width + self.height)

    def rect_diagonal(self):
        #returns the diagonal of the rectangle
        return math.sqrt((self.width ** 2) + (self.height ** 2))

    def __str__(self):
        #returns a formatted string showing the dimensions of the rectangle
        return (f"Rectangle's Dimensions"
                f"\n" + "-" * 40 +
                f"\nRectangle's Area: {self.rect_area():.2f} cm^2."
                f"\nRectangle's Perimeter: {self.rect_perimeter():.2f} cm."
                f"\nRectangle's Diagonal: {self.rect_diagonal():.2f} cm^2."
                f"\n" + "-" * 40)

