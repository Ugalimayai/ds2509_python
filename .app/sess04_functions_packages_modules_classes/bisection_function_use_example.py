# Python Script/file solving a problem requiring me to solve for the number of integers with a square root within epsilon of n

#import the bisection function
from bisection_search_sqrt_gt1 import bisection_root_positive_int

def count_nums_with_sqrt_close_to(n, epsilon):
    """n is an int/float
        epsilon is a positive number < 1
        returns how many integers have a square root within epsilon of n
    """
    count = 0
    #n ** 2 is the square of n, hence n ** 3 is a range big enough to find any digit whose square is within our desired epsilon of 0.1
    for i in range(n ** 3):
        #take the sqrt of i
        sqrt = bisection_root_positive_int(i)
        if abs(n - sqrt) < epsilon:
            #sqrt is within epsilon
            count += 1
            print(i, sqrt)

    return count

print(count_nums_with_sqrt_close_to(10,0.1))

