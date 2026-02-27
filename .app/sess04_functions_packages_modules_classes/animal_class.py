# Python file describing an animal class
# introduces the idea of getters and setters
# getters are used to return the values of the data attributes of an object
# setters are used to set a new value to the data attribute
# getters and setters should be used outside of class to access data attributes
# using getters and setters is a good coding practice. Using dot notation requires access to the class init method while the getter simply uses a method.
# while python allows you to create data attributes for an instance from outside the class definition it is NOT good programming practice
# writing getters and setters helps you avoid accessing and/or writing to data from outside the class definition

class Animal(object):
    def __init__(self, age):
        # initialise all data attributes
        self.age = age
        self.name = None #not every attribute has to be passed into the parameter list. This helps with inheritance
    def __str__(self):
        return "Animal:"+ str(self.name)+":"+str(self.age)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname



