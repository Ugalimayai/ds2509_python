# Python script to demonstrate simple comprehension operations on a list, set and dict
# a list of names and initials

names = ['John', 'James', 'Sam', 'Paul', 'Nemo', 'PAUL', 'J', 'memo']
print(f"Names and initials in the 'names' list are: \n{names}")

# Obtain a set of unique names that have more than one character using a set comprehension
names_set = {name[0].upper() + name[1:].lower() for name in names if len(name) > 1}

# Display the set of unique names
print(f"The unique names with more than one letter are:\n{names_set}")

# Dictionary of the occurrences of different letters in their lowercase and uppercase forms
test_dic = {'l':10, 'b':34, 'Z':2, 'N':4, 'L':4, 'z':5}

# Display the original dictionary
print(f"The original dictionary is: \n{test_dic}")

# get the total occurrences of each letter regardless of the case using a dict comprehension
letter_count = {
    k.lower(): test_dic.get(k.lower(), 0) + test_dic.get(k.upper(), 0)
    for k in test_dic.keys()
}

# Display the frequency for each letter
print(f"The letter count for the dictionary is: \n{letter_count}")
