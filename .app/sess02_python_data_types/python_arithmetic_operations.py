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



