# Python script to demonstrate OOP concepts of Data Hiding, method Overloading(simulation), and overriding

# Define an animal class

class Animal:
    def __init__(self, name, age):
        self._name = name #Protected by convention as an internal attribute

        self.__age = age # Private (name mangling to _Animal__age)

    def get_private_age(self):
        return self.__age # Access the private instance variable __age via a getter
    def speak(self):
        return f"{self._name} makes a sound"
    def make_sound(self, *args): # simulate overloading with *args(positional)
        base_sound = self.speak()
        if not args:
            return base_sound
        elif len(args) == 1 and isinstance(args[0], (int, float)):
            volume = args[0]
            return f"{base_sound} at volume {volume}"
        else:
            extras = ', '.join(str(args) for args in args)
            return f"{base_sound} with extras: {extras}"


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self): #Overriding the Animal's (parent class) speak method
        return f"{self._name} barks 'WOOF' loudly!"

# instantiate a dog obj and call the various methods
dog = Dog("Stones", 2)
print(dog.speak()) # overriding the Animals speak method
print(dog.make_sound()) # Overloading simulation: No arguments passed
print(dog.make_sound(8)) # Overloading simulation: volume argument of 8 passed
print(dog.make_sound(12, 'with toy', "excited")) # Overloading simulation: volume and extra *args passed
print(f"Stones age: {dog.get_private_age()} years.") # Data hiding: age accessed via getter
# print(dog.__age) # Error: Not directly accessible (but mangled: dog._Animal__age works)

