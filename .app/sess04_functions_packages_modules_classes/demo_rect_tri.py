# a python file/script to demonstrate the workings of the rectangle and triangle class
# import modules


from triangle import Triangle
from rectangle import Rectangle

# Prompt the user for the rectangle's width and height in (cm/m/ft/in)
height = float(input("Please enter the height of the rectangle in cm:\n"))
width = float(input("Please enter the width of the rectangle in cm:\n"))

# Create/ instantiate a rectangle object
rectangle1 = Rectangle(width, height)

# display the rectangles dimensions
print(rectangle1)

# Prompt the user for the triangle's sides in (cm/m/ft/in)
side_a = float(input("Please enter the length of the triangle's side 'a' in cm:\n"))
side_b = float(input("Please enter the length of the triangle's side 'b' in cm:\n"))
side_c = float(input("Please enter the length of the triangle's side 'c' in cm:\n"))

# Create/ instantiate a triangle object(radius)
triangle1 = Triangle(side_a, side_b, side_c)

# display the triangle's dimensions
print(triangle1)