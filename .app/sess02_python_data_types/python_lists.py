"""
Python Lists
A python list is a built-in data type that represents an ordered collection of elements that are homogeneous in nature.
Lists allow duplicates and are mutable(i.e. their elements can be modified, added or removed).
Lists are created using the [] or the list() constructor.
A sample list and some of its operations are given below.
"""

# Create a list of fruits
fruits = ["apple", "banana", "cherry", "mango", "grapefruit", "peach"]

#Display the fruits in the fruit list
print(f"The original fruits in the fruit list are: {fruits}")
# Display the number of items/elements in the fruit list
print(f"The number of fruits in the fruit list is: {len(fruits)}")

#Add a fruit to the end of the fruit list
fruits.append("orange")
print(f"After adding 'orange' to the fruit list we get: {fruits}")

#Add the contents of another list of fruits to our fruit list
fruits.extend(["pineapple", "avocado", "pears", "apple"])
print(f"The combined list of fruits is:\n {fruits}")

# Insert a fruit(item/element) at a given index
fruits.insert(1, "dragonfruit")
print(f"After inserting 'dragonfruit' to the fruit list we get: \n{fruits}")

#remove a fruit(item/element) from the list at a given index
removed_fruit = fruits.pop(3)
print(f"After removing {removed_fruit} from the fruit list we get:\n{fruits}")

#Remove fruit(Item/element) from the list by its name
fruits.remove("banana")
print(f"After removing 'banana' from the fruit list we get:\n{fruits}")

#get and display the index of a given item/element in the list
print(f"The first occurrence of 'mango' in the fruit list is at index: {fruits.index('mango')}")

#Get and display the occurrence(s) of a given item/element in the list
print(f"'apple' occurs {fruits.count('apple')} time(s) in the fruit list.")

#Sort and display the fruits in ascending/alphabetical/lexicographical order
fruits.sort()
print(f"After sorting the fruits list in ascending/lexicographical order we get: \n{fruits}")

#Sort and display the fruits in descending/reverse alphabetical order
fruits.reverse()
print(f"After sorting the fruits list in descending or reverse lexicographical order we get: \n{fruits}")

#Get and display the min and max item/element in the fruit list i.e. the least and highest fruits letterwise referenced from the ascii table
print(f"The least fruit letter-wise is {min(fruits)}")
print(f"The highest fruit letter-wise is {max(fruits)}")

#get and display a copy of the fruit list
copy_of_fruits = fruits.copy()
print(f"The copied list of fruits is: {copy_of_fruits}")

#remove all the fruits from the fruit list and display the empty list
fruits.clear()
print(f"After removing all fruits from the fruit list we get:\n{fruits}")

