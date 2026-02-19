class Coordinate(object):
    """
    Class Coordinate creates a coordinate object with two attributes: x and y
    the word object means that coordinate is a Python object and inherits all its attributes
    the init method is used to initialize some data attributes or perform initialization operations
    self refers to an instance of the class without having created one yet
    the (self.) is what allows us to create variables that belong to this object.
    Otherwise, we only create regular variables.
    a method is a procedural attribute. Basically a function that works only with this class.
    Convention is to use self as the name of the first argument of all methods

    """
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval

    def distance(self, other):
        """
        Returns euclidian distance between two Coordinate objects
        """
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def to_origin(self):
        """
        Always sets self.x and self.y to 0,0
        """
        self.x = 0
        self.y = 0



c = Coordinate(3, 4) # create a new object of type Coordinate and pass in 3 and 4 to the __init__
origin = Coordinate(0,0)

# we can then access the attributes of the created object
# data attributes of an instance are called instance variables
# the attributes were defined with self.XXX and are accessible using dot notation for the lifetime of the object

print(f"The x coordinate of the variable 'c' is: {c.x}")
print(f"The y coordinate of the variable 'c' is: {c.y}")
print(f"The x coordinate of the variable 'origin' is: {origin.x}")

# use the distance method. c is set as self and origin becomes 'other'
print(f"The distance between the variable 'c' and 'origin' is: {c.distance(origin)}") #this is similar to Coordinate.distance(c, origin)

d= Coordinate(12,50)
print(f"The coordinates of variable 'd' are: {d.x}, {d.y}")
d.to_origin()
print(f"After running the 'to_origin' method on d we get new coordinates: {d.x, d.y}")

