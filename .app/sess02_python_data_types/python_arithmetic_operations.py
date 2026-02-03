#python script/file to demonstrate the various arithmetic operations on numeric values

num1 = int(input('Enter the first number to be used in the calculation:\n'))
num2 = int(input('Enter the second number to be used in the calculation:\n'))

#Addition: Get the sum of the two numbers
summation = num1 + num2

#Difference/subtraction
difference = num1 - num2

#multiplication/product
product = num1 * num2

#Division: get the quotient of two numbers
floating_division = num1 / num2

integer_division = num1 // num2

#Modulus: Get the remainder of dividing the two numbers
modulus = num1 % num2

#exponentiation: Get the first number raised by the second
exponent = num1 ** num2

#Display results
print(f"Addition: {num1} + {num2} = {summation}")
print(f"Subtraction: {num1} - {num2} = {difference}")
print(f"Multiplication: {num1} * {num2} = {product}")
print(f"Floating Division: {num1} / {num2} = {floating_division}")
print(f"Integer Division: {num1} // {num2} = {integer_division}")
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Exponent: {num1} ** {num2} = {exponent}")


#square root approximation method to find a close enough square root
#floating point numbers cannot be represented in memory exactly hence operations on floats introduce tiny errors
#thus multiple operations on floats would magnify the errors
#we can then use an epsilon variable to check whether a solution yields a value within certain parameters/error bounds ( +- x)

x = 54321
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001
while abs(guess ** 2 - x) >= epsilon and guess ** 2 <= x:
    # (guess ** 2 - x) >= epsilon makes sure the algo stops when you are within epsilon
    # the guess **2 <= x stops the algo from going beyond the bounds of the required value
    guess += increment
    num_guesses += 1
print(f"num_guesses={num_guesses}")
if abs(guess ** 2 -x) >= epsilon:
    print(f"Failed on square root of, {x}")
else:
    print(f"{guess} is close to the square root of {x}")



