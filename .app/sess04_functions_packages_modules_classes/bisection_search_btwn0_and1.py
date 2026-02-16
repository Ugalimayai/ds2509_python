#for a number between 0 and 1
#multiplying a number between 0 and 1 by itself makes it smaller,
#thus the square root of the number between 0 and 1 is greater than the number itself
x = float(input("Enter a number between 0 and 1: "))
epsilon = 0.0001
# for numbers between 0 and 1, the highest value we can get is 1
high = 1
#the value cannot be lower than the starting point as the sqrt of the number is bigger than itself
low = x
guess = (high + low)/2.0
while abs(guess ** 2 - x) >= epsilon:
    if guess **2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0

print(f"{guess} is close to the square root of {x}")

