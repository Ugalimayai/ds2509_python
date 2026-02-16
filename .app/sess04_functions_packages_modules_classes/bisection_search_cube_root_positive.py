# Python code/script to demonstrate the use of bisection search to find the cube root of positive numbers

cube = 27
epsilon = 0.01
low = 0
high = cube
# the answer is between 0 and 27
guess = (low + high)/2.0
while abs(guess ** 3 - cube) >= epsilon:
    print(f"low: {low} high: {high} guess: {guess}")
    if guess ** 3 < cube:
        low = guess
    else:
        high = guess
    guess = (low + high)/ 2.0


print(f"{guess} is close to the cube root of {cube}")

