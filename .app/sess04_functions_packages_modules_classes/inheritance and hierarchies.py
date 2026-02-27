"""
The concept of inheritance in classes comes from having a parent class often referred to as a Superclass.
This superclass is associated with child class(es) that inherit all data and behaviors/methods of the superclass or parent class
They however, add more information, behaviors and sometimes can override the behavior specified for a parent class.
e.g for an animal superclass we can have subclasses like Person, Cat, Rabbit etc.
    They will all exhibit the same animal behavior e.g. being alive, having age, speaking
    but they will also have more behavior, e.g a human will speak in language while a cat will meow, a human will also be able to read etc
    a person can have more information like having friends
"""

#import the animal class
from animal_class import Animal
import random

# time to create our first subclass cat
class Cat(Animal):
    #our new class does not have an __init__ method because it inherits all methods from the parent class(Animal in this case)
    # we can now add more behavior with the speak method
    def speak(self):
        print("meow")
    def __str__(self):
        # we already have a __str__ method in the Animal class, however, we can override that and use this instead
        # it is accepted for it to have the same name as the superclass method
        return "cat:"+str(self.name)+":"+str(self.age)


# lets make a new person class
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends.copy()
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("konichiwassup")
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

p1 = Person("John", 25)
p2 = Person("Phil", 30)
# print(p1.get_name())
# print(p1.get_age())
# print(p2.get_name())
# print(p2.get_age())
# print(p1)
# p1.speak()
# p1.age_diff(p2)
# p1.add_friend('ana')
# p1.add_friend('bob')
# p1.add_friend('joe')
# print(p1.get_friends())


#function to map person object to cat object
def make_pets(d):
    """
    d is a dict mapping a Person obj to a Cat obj. Prints out on each line,
    the name of a person, a colon, and the name of the person's cat
    """
    for k, v in d.items():
        #k here is Person and v is Cat
        print(k.get_name() + ":" + v.get_name())


# c1 = Cat(5)
# c1.set_name("Puss in Boots") #using methods from the parent class
# c2 = Cat(1)
# c2.set_name("frrrrranky")
#
# d = {p1: c1, p2: c2}
# make_pets(d)

# Now with our initial superclass(Animal), we have established a subclass(Person),
# it is now time to introduce another subclass that inherits from both Animal and Person
class Student(Person):
    def __init__(self, name, age, major = None): # define our own init method in order to add a new (major) param
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def get_major(self):
        return self.major
    def speak(self):
        r = random.random()
        if r<0.25:
            print(" --> I have Assignments!")
        elif 0.25<=r<=0.5:
            print(" --> I need sleep!")
        elif 0.5<=r<=0.75:
            print(" --> I should eat!")
        else:
            print(" --> Steppin and Flexxin!")

    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":" +str(self.major)


# s1 = Student("John", 25, major="CS")
# s2 = Student("Phil", 12)
# s3 = Student("Chopper", 23, major="Medicine")
# print(s1)
# print(s2)
# print(s3)
# print(s1.get_major())
#
# print("{} says ".format(s3.get_name()))
# s3.speak()
# print("{} says ".format(s2.get_name()))
# s2.speak()
# print("{} says ".format(s1.get_name()))
# s1.speak()

# Let's make a new subclass under Animal for the sake of understanding class variables
# Class variables and their values are shared between all instances of a class

class Rabbit(Animal):
    tag = 1 # a class variable
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1 # when this instance changes the value of tag, it is updated across all instances
    def get_rid(self):
        return str(self.rid).zfill(5) #zfill pads the beginning of the number with zeroes
    def set_parent1(self, newname):
        self.parent1 = newname
    def get_parent1(self):
        return self.parent1
    def set_parent2(self, newname):
        self.parent2 = newname
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)

    def __str__(self):
        return "rabbit_id:" + self.get_rid() + " name:" + str(self.name) + " age:" + str(self.age) + " parent1:" + str(self.parent1) + " parent2:" + str(self.parent2)

r1 = Rabbit(1)
r2 = Rabbit(2, "Mike Wazowski", "Pole Position")
r3 = Rabbit(3)
print(r1)
r1.set_name("Jayden")
r1.set_parent1("Johnte Fatrabbit")
r1.set_parent2("Quela Slimqueen")
print(r1)
print(r2)
r4 = r1 + r2
print(r4)