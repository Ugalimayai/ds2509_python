# Python file/script to demonstrate recursion
"""
in recursion, we want to reduce a problem into a simpler/smaller version and have simple operations
in recursion, we have a recursive step that we are repeating and a base case which is a simple truth we know about
the problem we are trying to solve or the operator we are using.
The goal is to decrease and conquer the problem i.e. to reduce the problem into smaller versions of the same problem
or into a problem that can be solved directly.
semantically, it is a programming technique where a function calls itself. Since the goal is to not have infinite recursion
we must have 1 or more base cases that are easy to solve directly. Therefore, we must solve the same problem with different input
with the goal of reducing/simplifying the larger input problem and ending at the base case.
"""
# a simple multiplication function could be
def mult(a,b):
    return a*b

# however we can make this iterative
# we can define a * b as a + a + a + a ... b times

def mult_counter(a,b):
    total = 0
    for n in range(b):
        total += a
    return total

# another way is to have an iteration counter that starts at b and counts down to 0
def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

#now for recursion
def mult_recur(a,b):
    if b == 1:
        return a
    else:
        return a + mult_recur(a,b-1)

# function that calculates n**p
def power_recur(n,p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return n * power_recur(n,p-1)

#print(power_recur(2,5))

#recursive factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))
