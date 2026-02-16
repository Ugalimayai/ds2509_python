# this script/file demonstrates defining and calling/invoking user defined functions in python



#define a function to display a greeting message when called
def greeting(): #does not take any parameters
    print("Hello from 'greeting()' function!") #does not return any value as well

#call the greeting function
greeting()

#define a function that accepts a parameter (user's name) and greets the user
def greet_user(name):
    print("Hello %s from python functions" % name)

#prompt the user for their name
username =  input("Please enter your name:\n")
#call the greet_user func
greet_user(username)

# define a function that accepts two numbers and a '+' (-> default) or 'x' operator to add or multiply them respectively
def add_or_multiply(first_num, second_num, operation = '+'):
    """
    This function adds or multiplies two numbers depending on the operation specified

    :param first_num(int): the first number to be used in the calculation.
    :param second_num(int): the second number to be used in the calculation.
    :param operation(str, optional): the operation to be performed. Defaults to '+'.
    :return int: the sum or product of two numbers.
    :raises
        None
    Examples:
        >>> add_or_multiply(1,2)
        3
        >>> add_or_multiply(2,2, operation='*')
        4
        >>> add_or_multiply(1,2, operation='/')
        Invalid operation!
        Please use '+' or 'x'
    """
    if operation == '+':
        return first_num + second_num
    elif operation == '*' or operation == 'x':
        return first_num * second_num
    else:
        print("Invalid operation!\nPlease use '+' or 'x'")
        return #user gave us an invalid operator,we stop further execution

#invoke the add_or_multiply() function
print(f"The sum of 3 and  is {add_or_multiply(3,5)}")
print(f"The product of %d and %d is %d" %(3,5, add_or_multiply(3,5, operation='*')))

#display the documentation string of the function
print(f"The documentation string of the 'add_or_multiply' function is {add_or_multiply.__doc__}")

#anonymous functions
#an anonymous function/lambda function is a way to write small compact functions quickly. They are often used when
#you need a simple function for a short period and don't want to write a full function using the def keyword

plus_five = lambda num: num + 5 #use lambda to add five to a number
print(f"The sum of 7 and 5 using a lambda function is : {plus_five(7)}")

# the same functionality using a normal function
def add_five(num):
    return num + 5

# call/invoke the add_five function
print(f"The sum of 2 and 5 is: {add_five(2)}")

#anonymous function to get the difference between two numbers
difference = lambda num1, num2: num1 - num2
print(f"The difference between 2 and 5 is: {difference(2,5)}")

#function with variable number of arguments
# define a function that accepts a varying number of parameters
def get_sum(*values):
    #sum = 0
    #for value in values:
    #    sum += value
    #return sum
    """

    This function returns the sum of all the values passed in.
    Args:
        *values: Variable number of arguments/numbers/values to be summed.
    Returns:
        int or float: the sum of all the values passed in.
    Raises:
        TypeError: if any of the arguments is not an int/float.
    Examples:
        >>> get_sum(1,2,3)
        6
        >>> get_sum(3.5,2.1,1.4)
        7.0
        >>> get_sum(1,2,"3")
        TypeError: All values provided must be numbers/numeric values.

    """
    try:
        return sum(values)#succint code
    except TypeError as e:
        raise TypeError("All values provided must be numbers/numeric values.") from e

#create  list of numbers
num_list = [1,2,3,4,5,6,7,8,9,10]
print(f"The sum of the first ten numbers is:{get_sum(*num_list)}")
nums_with_decimals = [4.5,1.5,2.0]
print(f"The sum of 4.5, 1.5, and 2.0 is: {get_sum(*nums_with_decimals)}")
mixed_nums = [2,5,'7']
print(f"The sum of 2, 5, and '7' is: {get_sum(*mixed_nums)}")
