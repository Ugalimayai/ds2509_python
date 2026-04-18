# Python script to demonstrate the use of a closure to multiply a parameter with a second value
# is closure ust an implementation of nested functions...is it even good practise?

# Define the enclosing function
def multiplier(n):
    def inner(x):
        return x * n
    return inner

# Create 2 multiplier function
triple = multiplier(3)
quadruple = multiplier(4)

# Use the above enclosures to triple 5 and quadruple 8
print(f"5 tripled is: {triple(5)}")
print(f"8 quadrupled is: {quadruple(8)}")


