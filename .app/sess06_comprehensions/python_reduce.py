# Python file to demonstrate use of the 'reduce' function

#import required modules
from functools import reduce

# a list of numbers to be manipulated using the 'reduce()' function
numbers = [17,45,23,68,9]

# get the largest number from the numbers list using the reduce() function
largest_num = reduce(lambda x, y: max(x, y), numbers)

# get the least number from the numbers list using the reduce() function
least_num = reduce(lambda x, y: min(x, y), numbers)

# obtain the product of the numbers in the list using the reduce() function
product_of_nums = reduce(lambda x, y: x * y, numbers)

# Display the results
print(f"The list of number is:\n{numbers}")
print(f"The largest number is:\n{largest_num}")
print(f"The least number is:\n{least_num}")
print(f"The product of numbers is:\n{product_of_nums}")
