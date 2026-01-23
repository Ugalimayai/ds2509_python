#python script/file to demonstrate working with strings

#declare a string variable

string_var = "hello Ephraim from Python programming"

#display the above string with the first letter in uppercase using % and an f-string
print(f"'string_var' with the first letter capitalised is: %s." % string_var.capitalize())
print(f"'string_var' with the first letter capitalised is: {string_var.capitalize()}.")

#display the type of 'string_var'
print(f"The type of 'string_var' is: {type(string_var)}")

#display the contents of 'string_var' in uppercase using .upper()
print(f"The contents of 'string_var' are: {string_var.upper()}.")

#display the contents of string in lowercase using lower()
print(f"The contents of 'string_var' are: {string_var.lower()}.")

string_2_center = "Programming"
#center the above text with a specified width and given fill character
print(string_2_center.center(30,'*'))

#display the number of times a particular character 'o' appears in the string using the .count() function
print(f"The letter 'o' appears {string_var.count('o')} times in the string.")

#display the highest and lowest alphabetical characters in 'string_var'
print(f"The highest alphabetical character in the string is {max(string_var)}")
print("The highest and lowest alphabetical character in the string are" " %s & %s respectively!" %(max(string_var), min(string_var)))

#replace the 'hello' with 'hallo' and 'Python' with 'C++'
new_str = string_var.replace("hello", "hallo")
new_str = new_str.replace('Python', 'C++')
#display the new string
print(new_str)

#declare another string variable for more string operations
my_string = "   Hello, World! 123   "

#len() - return the length(no. of characters) in the string
print(f"Length of the string 'mystring' is: {len(my_string)} characters.")

#isalnum() checks if all characters are alphanumeric (no spaces and special characters/symbols)
print(f"Is the string '{my_string}' alphanumeric?\n{my_string.isalnum()}")

#islower() to check if all characters are lowercase
print(f"Is the string '{my_string}' all lowercase? \n{my_string.islower()}")
print(f"Is the string '{my_string}' all uppercase? \n{my_string.isupper()}")

# lstrip() removes any leading whitespaces(from the left side of the string/text)
print(f"Remove the leading spaces from '{my_string}' to get \n{my_string.lstrip()}")

#rstrip() removes any trailing whitespaces (from the right side of the string/text)
print(f"Remove the trailing spaces from '{my_string}' to get \n{my_string.rstrip()}")

#strip() removes any leading and trailing whitespaces (from the left and right side of the string)
print(f"Remove the leading and trailing whitespaces from '{my_string}' to get \n{my_string.strip()}")

# check if the string ends with a specified substring
print(f"Does the string '{my_string}' end with '123   '?\n{my_string.endswith('123   ')}")

#startswith() checks if a string starts with a particular substring
print(f"Does the string '{my_string}' start with '   Hello'?\n{my_string.startswith('   Hello')}")
print(f"Does the string '{my_string}' start with 'Hello'?\n{my_string.startswith('Hello')}")

# find() locates the first occurrence of a specified substring
print(f"The first occurrence of the string 'World' in {my_string} is at index"
      f": {my_string.find('World')}") #returns -1 if the substring is not found

# index() finds the first occurrence of the substring specified, raises an error if not found
print("Index of 'World' in %s is at index %d" %(my_string, my_string.index('World')))

# count() returns the number of occurrences of the substring
print("The number of occurrences of 'l' in %s is %d" %(my_string, my_string.count('l')))

# rfind() this is 'reverse-find' - returns the last occurrence of the specified substring
print(f"The last occurrence of 'l' in {my_string} is at index {my_string.rfind('l')}")

#rindex() returns the last occurrence of a substring,raises an error if not found
print("The last index of 'l' in %s is at index %d" %(my_string, my_string.rindex('l')))



