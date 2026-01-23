"""
Python Dictionaries
A python dictionary is a built-in data structure that stores key-value pairs
Dictionaries are unordered, mutable and can store elements of different types
Each element in a dictionary is accessed by its key rather than its index.
Dictionaries are created using the curly brackets{}
"""

# student dictionary declaration
student = {"name": "Abigail", "age": 25, "major": "Computer Science"}

#Display the length (number of key-value pairs) in the student dict
print(f"The number of key-value pairs in the student dictionary is {len(student)}")

#fetch and display a view object(method to get the keys of a value from a dict)
print(f"The keys from the student dict are:\n{student.keys()}")

# fetch and display the view object of the values in the student dict
print(f"The keys from the student dict are:\n{student.values()}")

#get a value from the student dict using the key
print(f"The key 'name' in the student dict points to: {student.get('name')}")

#remove contents of a given key when it exists in a dictionary, else return an optional default value
phone_no = student.pop('phone_no', "Not Specified")
print(f"The value of 'phone_no' in the student dict is: {phone_no}")

#remove and display the contents of the last key-value pair in the dict
print(f"The last key-value pair in the student dict is: {student.popitem()}")

#update/modify and display the contents of the dict
student.update({"age":21, 'grade':'A', 'phone': "0721123547"})
print(f"The updated contents of the student dict are:\n{student.items()}") #or simply {students}

#create and display a copy of the student dict
copy_of_student = student.copy()
print(f"The contents of 'copy_of_student' are:\n{copy_of_student}")

# fetch and return the value associated with a given key, and when not found assign it a default value
major = student.setdefault('major', "Not Specified")
print(f"The value of 'major' in the student dict is: {major}")

# Create and display a new dictionary from the keys  of an existing dictionary
new_student = dict.fromkeys(student.keys(), "")  # new_student = dict.fromkeys(["name","age","grade"])
print(f'The key-value pairs in the "new_student" dictionary are:\n{new_student}')

# Delete a specific key-value pair from the "student" dictionary
# and display the remaining key-value pairs
del student['grade']
print(f'After deleting/removing the "grade" key from the "student" dictionary, '
      f'the remaining key-value pairs are:\n{student}')

# Find out and display whether a given key exists/is present in a dictionary
print(f'The key "age" is present in the "student" dictionary: {"age" in "student"}.')
print(f'The key "grade" is present in the "student" dictionary: {"grade" in "student"}.')

# Remove all contents from the student dictionary
student.clear()
print(f'After clearing the "student" dictionary, we get:\n{student}')


