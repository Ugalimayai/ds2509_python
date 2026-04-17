# Python script to demonstrate the use of formal, positional and keyword arguments
# in a function

# Function definition
def profile(name, *args, **kwargs):
    print(f"Name: {name}") #Formal argument
    if args: # positional variable argument
        print(f"Hobbies: ")
        for hobby in args:
            print(f"- {hobby}")
    if kwargs: #keyword variable arguments
        print(f"Other info. :")
        for key, value in kwargs.items():
            print(f"- {key}: {value}")

profile("Mwaniki", "Reading, Travelling, Video Games, Football, Youtube, Hiking", gender="Male", age=25,
        weight=70, job="Student", city="Nairobi", county="Kiambu", country="Kenya")

#NB
# 1. Formal arguments :- are defined in the function signature(name in profile function)
# 2. *args :- collects positional arguments as a tuple
# 3. **kwargs :- collects keyword arguments as a dictionary
