"""
Python Sets
A python set is a built-in data type that represents an UNORDERED COLLECTION of elements of the same or different types
sets DON'T allow duplicates but are mutable and are useful for tass that involve checking membership, removing duplicates and performing mathematical set operations like
intersection, union, difference, and symmetric difference.
Sets are created using the curly braces {} or the set() constructor

"""

#create a set of fruits
fruits = {'apple', 'banana', 'cherry', 'durian', 'elephant apple'}

#display the contents of the fruits set
print(f"The contents of the 'fruits' set are: {fruits}")

#display the number of fruits in the set
print("The number of fruits in the fruits set is: %s" % len(fruits))

# add orange to the set of fruits
fruits.add('orange')

# display the new set
print(f"After adding 'orange' to the set of fruits, we get:\n{fruits}")

#remove banana from the set of fruits
fruits.remove('banana') #returns an error if the element is not in the set

# display the resultant set
print(f"After removing banana from the set we get:\n{fruits}")

#discard a fruit from the set and display the remaining fruits
fruits.discard('cherry')
print(f"After discarding cherry from the set we get:\n{fruits}") #does not return an error if the element is not in the set

# remove the last fruit from the fruit set
popped_fruit = fruits.pop()
print(f"After popping '{popped_fruit}' from the set we get:\n{fruits}")

# declare another set of fruits
more_fruits = {'pear', 'avocado', 'mango', 'pineapple'}

# create a combined set off fruits and display it
combined_fruits = fruits.union(more_fruits)
print(f"The combined set of fruits is:\n{combined_fruits}")

#copy the remaining set of original fruits and display them
copy_of_fruits = fruits.copy()
print(f"After copying the remaining fruits into a new set we get:\n{copy_of_fruits}")

# get and display the common fruits in the 'fruits' and 'more_fruits' sets
common_fruits = fruits.intersection(more_fruits)
print(f"The common fruits in 'fruits' and 'more_fruits' are:\n{common_fruits}")

# get and display the fruits that are in the 'fruits' set but not in the 'more_fruits' set
difference_fruits = fruits.difference(more_fruits)
print(f"The fruits that are in the 'fruits' set but not in the 'more_fruits' set are:\n{difference_fruits}")

# Get and display the fruits that are either in 'fruits' or in 'more_fruits' set but not both
symmetric_difference_fruits = fruits.symmetric_difference(more_fruits)
print(f"The fruits that are either in 'fruits' or in 'more_fruits' but not in both are:\n{symmetric_difference_fruits}")

#check whether 'fruits' set is a subset of 'more_fruits' set
is_subset_of_more_fruits = fruits.issubset(more_fruits)
print(f"'fruits' set is a subset of 'more_fruits' set: {is_subset_of_more_fruits}")

#check whether 'fruits' set is a superset of 'more_fruits' set
is_superset_of_more_fruits = fruits.issuperset(more_fruits)
print(f"'fruits' is a superset of 'more_fruits' set: {is_superset_of_more_fruits}")

# check and display whether 'fruits' set and 'more_fruits' sets have no common fruits/elements
is_disjoint_fruits = fruits.isdisjoint(more_fruits)
print(f"'fruits' set and 'more_fruits' have no common fruits/elements: {is_disjoint_fruits}")

#create another fruit set and use it to update the set of 'fruits'. CAUTION ... this overwrites set elements
other_fruits = {'watermelon', 'strawberry', 'blueberry'}
fruits.update(other_fruits)
print(f"After updating the 'fruits' set we get:\n{fruits}")

# clear and display the fruits set
fruits.clear()
print(f"After clearing the fruits set we get:\n{fruits}")












