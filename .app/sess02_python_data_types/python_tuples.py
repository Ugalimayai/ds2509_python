"""
a tuple is a built-in data type that represents an  indexable ordered collection of elements
tuples allow duplicates and are immutable(the elements cannot be modified)
tuples are created using () rounded brackets/parentheses or the tuple() function
tuples are generally faster than lists as python doesn't have to worry about growing or  shrinking tuples
"""
#a tuple of fruits
fruits =  ('blueberry', 'orange', 'apple', 'banana', 'avocado', 'guava', 'blueberry')

#display the length i.e number of fruits in the tuple
print(f"The number of elements/items in the fruits tuple is: {len(fruits)}")

#get and display the names of the fruits in the tuple
print(f"The fruits in the tuple are:\n{fruits}")

#get and display the index of an item/element in the tuple
print(f"The index of 'avocado' in fruits is: {fruits.index('avocado')}")

#get and display the number of occurrences of 'blueberry'
print(f"The fruit 'blueberry' appears {fruits.count('blueberry')} times in the fruits tuple.")

# combine two tuples to create a third one and display its contents
combined_fruits = fruits + ('kiwi', 'watermelon', 'pineapple', 'dragon fruit')
print(f"Combined fruits tuple contains:\n {combined_fruits}")

#create a tuple that repeats the fruit tuple twice
fruits_repeated = fruits * 2
print(f"The fruits repeated tuple contains:\n {fruits_repeated}")

# create a sorted tuple of fruits
sorted_fruits = sorted(fruits)
print(f"The fruits sorted tuple contains:\n {sorted_fruits}")

#Display the minimum and maximum items in the fruits tuple
print(f"The least fruit letterwise is: {min(fruits)}")
print(f"The highest fruit letterwise is: {max(fruits)}")

# declare a tuple of numbers
numbers = (1,2,3,4,5)

#display the tuple of numbers and its sum
print(f"The 'numbers' tuple contains: {numbers} and their sum is: {sum(numbers)}")

#display the first three numbers in the tuple using slice
print(f"The first three numbers in the tuple are: {numbers[:3]}") #same as numbers[0:3]

#display all the odd numbers in the numbers tuple using slice
print(f"The odd numbers in the 'numbers' tuple are: {numbers[::2]}") #same as numbers[0::2]

#use the 'any()' function to check if any element in the numbers tuple is true
# in python, non-zero numbers are considered true. Since all numbers in the tuple are non-zero,
#any() will return true

any_true = any(numbers)
print(any_true) #this should print true as there are no non-zero values/elements in the numbers tuple

#use the all() function to check if all elements are true
#will return true as all values in the numbers tuple are non-zero
all_true = all(numbers)
print(all_true)

# a tuple can have a nested tuple inside it

seq = (2,'a', 4, (1,6,7,8,23,3), 77)
print(f"The nested tuple inside our 'seq' tuple is: {seq[3]}")
print(f"We can slice inside our nested tuple: {seq[3][0:3]}")

#we use tuples to conveniently swap variable values
x = 1
y = 2
print(f"The value of x is: {x}")
print(f"The value of y is: {y}")
(x,y) = (y,x) #this is more convenient than first creating a temp variable to hold values
print(f"After swapping using tuple assignment, the value of x is %s and the value of y is %s" % (x,y))

#we can also use tuples to return more than one value from a function
def char_counts(s):
    """
    s is a string of lowercase chars
    returns a tuple where the first value is the number of vowels in s
    and the second value is the number of consonants in s
    """
    s = s.strip().lower()
    vowels = ('a','e','i', 'o', 'u')
    consonant_count = 0
    vowel_count = 0
    for i in s:
        if i in vowels:
            vowel_count += 1
        elif i == " ":
            pass
        else:
            consonant_count += 1

    return (vowel_count, consonant_count)
text = "Return of the Mac"
print(f"The number of vowels in {text} is {char_counts(text)[0]}"
      f" and the number of consonants in {text} is {char_counts(text)[1]}")

