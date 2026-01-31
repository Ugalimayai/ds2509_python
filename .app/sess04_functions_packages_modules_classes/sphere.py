# Python file/script to define a Sphere class that inherits from the Circle class

#import the required modules

from circle import Circle

class Sphere(Circle):
    def __init__(self, radius):
        super().__init__(radius)

    def calc_surface_area(self):
        return 4.0/3.0 * self.calc_area()

    def calc_volume(self):
        return 4.0/3.0 * self.calc_area() * self.radius

    def __str__(self):
        """
        Returns a formatted string detailing the sphere's dimensions.
        Returns:
        -----------------
        str
            A readable summary of the radius, surface area, and circumference of the sphere.
        """
        return (f"Sphere's Dimensions"
                f"\n" + "-" * 40 +
                f"\nRadius: {self.radius} cm."
                f"\nSurface Area: {self.calc_surface_area():.2f} cm^2."
                f"\nVolume: {self.calc_volume():.2f} cm."
                f"\n" + "-" * 40)
