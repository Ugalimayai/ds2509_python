# Python script to get a persons details from the user then store them in the 'person.txt' file
# in the 'files' folder/directory using the 'pickle' module

# Import required modules
import pickle
import os
from person import Person

# Prompt the user for their name, age, gender
name = input("Please enter your name:\n")
age = input("Please enter your age:\n")
gender = input("Please enter your binary using 'm' for male & 'f' for female:\n")

# Create/instantiate a Person object
user = Person(name, age, gender)

# Get the path to the file to be created
file_path = os.path.abspath(os.path.join(os.getcwd(),"..","files","person.txt"))

# Pickle the 'Person' object
with open(file_path, 'ab') as file:
    pickle.dump(user, file)

print(f"The 'user' object has been pickled successfully in:\n{file_path}")
