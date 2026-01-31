# Python script/file to demonstrate working with user defined/ custom classes
# and instantiating them
#import the required modules

from circle import Circle
from sphere import Sphere

# Prompt the user for the circle's radius in (cm/m/ft/in)
radius = float(input("Please enter the radius of the circle in cm:\n"))

# Create/ instantiate a circle object
circle1 = Circle(radius)

# display the circles dimensions
print(circle1)

# Prompt the user for the sphere's radius in (cm/m/ft/in)
radius = float(input("Please enter the radius of the sphere in cm:\n"))

# Create/ instantiate a sphere object(radius)
sphere1 = Sphere(radius)

# display the circles dimensions
print(sphere1)


