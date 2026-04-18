# Python script to demonstrate the use of  a closure to increment a counter and return its value

# Define a closure function
def counter():
    count = 0
    # Define an inner function ( the return obj of the enclosing function)
    def inner():
        nonlocal count # refers to the count in the enclosing function
        count += 1
        return count
    return inner

# create two counter instances
c1 = counter()
c2 = counter()

# Display the return type for the counter() function
print(f"The counter function returns: {type(c1)}")

# Display the first 10 values using c1 for loop
for n in range(10):
    print(f"Current value of counter is: {c1()}")

# Display the first 5 values of 'c2' manually
print(f"Values for counter 2 are:")
print(f"Current value of counter 2 is: {c2()}")
print(f"Current value of counter 2 is: {c2()}")
print(f"Current value of counter 2 is: {c2()}")
print(f"Current value of counter 2 is: {c2()}")
print(f"Current value of counter 2 is: {c2()}\n")

# Display the subsequent value of 'c1'
print(f"Current value of counter 1 is: {c1()}")