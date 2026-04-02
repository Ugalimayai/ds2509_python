# Python script to demonstrate function decorators

# Function to get the nth Fibonacci number using recursion

def fibonacci(n):
    """
    Calculates the nth Fibonacci number using recursion
    :param n: (int): The nth Fibonacci number
    :return: (int): The fib number at position n
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# fibonacci() function decorator
def fib_decorator(func):
    """
    Decorator function that adds a print statement before and after executing the function
    :param func(function): the function to be decorated:
    :return: The wrapper function
    """
    def wrapper(n):
        print("Calculating Fibonacci numbers")
        result = func(n)
        print(f"Fibonacci numbers are:\n{result}")
        return result
    return wrapper

# make use of the above decorator
@fib_decorator
def generate_fibonacci_number(n):
    """
    Generate a list of fibonacci numbers
    :param n(int): The nth Fibonacci number
    :return(list): A list of fibonacci numbers
    """
    return [fibonacci(a) for a in range(n)]

# call/invoke the generate_fibonacci_numbers() function to generate the first 7 fib numbers
generate_fibonacci_number(7)
print('\n')
generate_fibonacci_number(18)
print('\n')

