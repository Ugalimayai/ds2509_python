# This script/file demonstrates Python's iteration/repetition/looping constructs

# 1. for loop
# create a list of fruits
fruits = ["avocado", "durian", "elephant apple", "mango", "fig", "guava","cherry", "banana"]

# display each of the above fruits using a for loop
for fruit in fruits:
    print(f"The current fruit is: {fruit}")

#create a tuple of numbers and display them using a for loop
numbers = (8,2,5,7,6,2,3,40,12,22,39,100,23,324334,12323,446663,99)

# display each of the numbers using a loop
for number in numbers:
    print(f"The current number is: {number}")

# 2. Range
print(f"range".center(50,"-"))

# basic range: generate the first 5 numbers
for n in range(5): #basic range starts from 0 to the specified number minus one (n-1)
    print(f"The current number is: {n}\n")

print(f"Range with Parameters".center(50,"~"))
#Generate even numbers starting from 2 to 10(exclusive) using range() with start, stop, and step values
for n in range(2,10,2):
    print(f"The current even number is: {n}")

# display the cubes of the first five integers using a ranged for loop and list comprehension
cubes = [n **3 for n in range(1,6)]
print(f"The cubes of the first five numbers/integers are:\n{cubes}")

# 3. while loop
print(f"while loop".center(50,"-"))
# display the first five multiples of eight
n=1
print("The first five multiples of 8 are:")
while n<=5:
    print("%d x 8 = %2d" % (n, n*8)) # %d is a format specifier for integers
    #print(f"{n} x 8 = {n*8}")
    n += 1

# create a list of odd numbers between 1 - 19
n, odd_nums = 1, []
print(f"The odd numbers between 1 - 19 are:")
while n <=19:
    #if n % 2 == 1: # same as n != 0
     #   odd_nums.append(n)
    if n % 2 ==0:
        n += 1
        continue # skip the current iteration when the number is even
    odd_nums.append(n)
    n += 1

# Display the list of odd numbers
print(odd_nums)

#practical use of the while loop to search for some text in a paragraph
paragraph = """
To change the way a picture fits in your document,click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign. Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device. Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries. Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme. Save time in Word with new buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for layout options appears next to it.
"""
# variable to hold the word/text to search for
text_to_search = "ds2509"
found = False #variable to indicate whether the search term was found or not
index =0
while index < len(paragraph):
    #find the index of the word/search text
    if paragraph[index: index + len(text_to_search)] == text_to_search:
        found = True
        break # exit from while loop when target is found
    index += 1
if found:
    print(f"The text/word '{text_to_search}' was found at index {index}.")
else:
    print(f"The text/word '{text_to_search}' was not found in the paragraph.")

