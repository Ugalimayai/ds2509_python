# Python file/script to define a 'circle' class

#import the in-built math module
import math #allows us to access the in-built value of pi and pow() function

class Circle:
    """
    A class to represent a 2-D geometric circle.

    Attributes:
    ------------------
    radius: float
        The radius of the circle

    Methods:
    ------------------
    calc_area():
        Calculates and returns the area of the circle.
    calc_circumference():
        Calculates and returns the circumference of the circle.

    __str__():
        Returns a formatted string detailing the circle's dimensions.
    """
    def __init__(self, radius = 0): #creates a circle with a default radius of 0
        """
        Initializes the circle with the given radius.
        Attributes:
        ------------------
        radius: float, optional
            The radius of the circle (defaults to 0)
        """
        self.radius = radius

    def calc_area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
        ------------------
        float
            The area of the circle using the formula: π * r²
        """
        #return math.pi * self.radius ** 2 #same as code below
        return math.pi * math.pow(self.radius, 2)

    def calc_circumference(self):
        """
        Calculates and returns the circumference of the circle.
        Returns:
        -----------------
        float
            The circumference of the circle using the formula: π * (2 * r)
        """
        return math.pi * (self.radius * 2)

    def __str__(self): #dunder(double underscore) method
        """
        Returns a formatted string detailing the circle's dimensions.
        Returns:
        -----------------
        str
            A readable summary of the radius, area, and circumference of the circle.
        """
        return (f"Circle's Dimensions"
                f"\n"+ "-" * 40 +
                f"Radius: {self.radius} cm."
                f"\nArea: {self.calc_area():.2f} cm^2."
                f"\nCircumference: {self.calc_circumference():.2f} cm."
                f"\n" + "-" * 40)

