#Python script to demonstrate 're' modules methods

# import the modules
import re

print("=" * 50 )
print("re.match() demonstration")
print("=" * 50 )
print("re.match(): check for a match only at the beginning of a string."
      "\nReturns a match object if found.")
text = "Hello World"
pattern = r"Hello"
result1 = re.match(pattern, text)
result2 = re.match(r"World", text)

if result1:
    print(f"Trying to match 'Hello' at the start of {text}: Found!")
else:
    print(f"No match found: {result1.group()}")

print(f"Trying to match 'World' at the start of {text}: {result2}")

print("=" * 50 )
print("re.search() demonstration")
print("=" * 50 )
print("re.search(): searches an entire string for the first occurrence of the pattern.\n")
text = "This sentence leads to the most-popular phrase for programming padawans: 'Hello World'"
pattern = r"Hello"

result = re.search(pattern, text)
if result:
    print(f"Match found: {result.group()} at position (starting from 0): {result.start()}")
else:
    print(f"No match found: {result.group()}")

print("=" * 50 )
print("re.findall() demonstration")
print("=" * 50 )
print("re.findall(): Returns all non-overlapping matches as a list.\n")
text = "The rain in Spain falls mainly in the plain."
pattern = r"in"

result = re.findall(pattern, text)
print(f"The word {pattern} was found in {len(result)} matches.\n{result}")

# Example to extract emails from text
text = ("John said he got the following emails from the client.(test email) a.nyanjui.ac.ke From client1, test1@email.com,"
        "from client2, testemail@ymail.com, and from client3, test3@outlook.com")
pattern = r"\w+\.*@*\w+\.+\w+\.*\w+"
print(f"The emails extracted from John's text are:\n{re.findall(pattern, text)}")

print("=" * 50 )
print("re.split() demonstration")
print("=" * 50 )
print("re.split(): splits the string whenever the pattern matches.\n")

text = "grape avocado, grape; orange apple, mango; cherry"
pattern = r"[ ,;]+"
fruits = re.split(pattern, text)
print(f"The fruits extracted from the text are:\n{fruits}")


print("=" * 50 )
print("re.sub() demonstration")
print("=" * 50 )
print("re.sub(): replaces all or specified number of occurrences of the pattern with a replacement string.\n")
text = "The price of petroleum is Kes. 206 and diesel is Kes. 209."
pattern = r"\d+"

# replace the numbers with '***'
result = re.sub(pattern, "***", text)
print(f"The result of number replacement is:\n{result}")

# re.sub accepts a function as an argument
# Example with function replacement
def double_number(match):
    number = int(match.group())
    return str(number * 2)

text = "Numbers: 3 8 5 12 7"
result = re.sub(pattern, double_number, text)
print(f"The result of double number replacement is:\n{result}")