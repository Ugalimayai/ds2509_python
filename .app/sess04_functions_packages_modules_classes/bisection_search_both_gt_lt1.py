x = float(input("Enter a positive number:"))
epsilon = 0.0001
if x>=1:
    low = 1.0
    high = x
else:
    low = x
    high = 1.0

guess = (low + high)/2.0

while abs(guess **2 -x) >= epsilon:
    print(f"low: {low} high: {high} guess: {guess}")
    if guess ** 2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/ 2.0

print(f"{guess} is close to the square root of {x}")
