# Python script to unpickle the person's details from the 'person.txt' file

# import the required modules
import pickle, os

# variable to hold the path to the 'person.txt' file
file_path = os.path.abspath(os.path.join(os.getcwd(),"..","files","person.txt"))

# list that will hold the 'Person' object from the person.txt file
persons = []

# Open the 'person.txt.' file and read its contents
with open(file_path, 'rb') as f:
    while True:
        try:
            unpickled_person = pickle.load(f)
            persons.append(unpickled_person)
        except EOFError:
            break # End of file reached

# Access and display the pickled person's details/attributes
if persons:
    print(f"Details of the person in the 'person.txt' file")
    print(f"-" * 60)
    for index, person in enumerate(persons, start=1):
        print(f"Person {index}. Name: {person.name}, Age: {person.age}, Gender: {person.gender}")
    print(f"-" * 60)
else:
    print("There are no persons in the 'person.txt' file")
