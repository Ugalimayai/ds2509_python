#Python file/script to show using functions as a parameter
#Python treats functions as objects and functions can then be called as parameters


def apply(criteria, n):
    """

    :param criteria: Criteria is a func that takes in a number and returns a bool
    :param n: an int
    :return: returns how many ints from 0 to n(inclusive) match the criteria.
    (i.e. return True when run with criteria)
    """
    count = 0
    for i in range(0, n+1):
        if criteria(i):
            count += 1
    return count

def is_even(x):
    return x % 2 ==0

def is_five(x):
    return x == 5

dex = apply(is_five, 10)
print(dex)
