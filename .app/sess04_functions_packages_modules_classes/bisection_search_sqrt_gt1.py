#Bisection Search
"""
We can apply bisection search to problems with an inherent order to the range of possible answers.
Supposing we know the answer lies within some interval:
    we guess the midpoint of the interval
    if not correct, we check whether the answer is greater than or less than the midpoint
    we change the interval
    repeat
This process cuts the set of things to check in half at each stage:
    exhaustive search reduces them from N to N-1 on each step
    bisection search reduces them from N to N/2

Checking answers one-on-one is linear in terms of possible guesses
checking answers by guessing the halfway point is logarithmic on the number of possible guesses
"""


#let's use bisection search for a square root problem
"""
if we are looking for the square root of number and we know the answer is between 0 and x 
and we make a guess g where g is halfway between 0 and x
if g **2 is greater than x,
then we half the search space and the answer is between 0 and g
we now make a guess new_g which is the midpoint of 0 and g
if new_g **2 is less than the target x, 
we half the search space again and the answer is between new_g and g
we repeat the process iteratively and keep reducing the range of values to search by half 
"""
#x = float(input("Enter a number that's greater than 1: "))
#epsilon = 0.0001

def bisection_root_positive_int(x):
    """
    :param x: int or float greater than 1
    :param epsilon: accuracy argument x<1>0
    :return: float value guess of most accurate sqrt
    """
    epsilon = 0.001
    #num_guesses = 0
    low = 0
    high = x
    guess = (high + low)/2.0
    while abs(guess ** 2 - x) >= epsilon:
        #print(f"low: {low}, high: {high}, guess: {guess}\nnumber of guesses: {num_guesses}")
        if guess **2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0

        #num_guesses += 1

    return guess

#print(f"{bisection_root_positive_int(10)} is close to the square root of 10")

