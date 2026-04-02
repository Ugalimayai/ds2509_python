#Python script to demonstrate filter() function

# list of fibonacci numbers
numbers = [1,1,2,3,5,8,13,21,34,55,89,144]

# get and display list of even Fib numbers using filter
even_fibonacci = list(filter(lambda x: x% 2 == 0, numbers))
print(even_fibonacci)

# set of student names
student_names = {"Abigail", "Bernice", "Joe", "Denise", "Sue", "Jim", "Mark","Micha","William","Jane","Xi","Alfred", "Hillary", "Anthony","Brigid", "Mitchell","Alice"}

#Filter and display the names starting with letter 'A'
filtered_names = list(filter(lambda name: name.startswith("A"), student_names))
print(f"All Student names:\n{student_names}\nFiltered names:\n{filtered_names}")

# Function to determine primeness of a number
def is_prime(n):
    """

    Check if a given number is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors
    other than 1 and itself.

    Args:
    n (int): The number to be checked. Must be a non-negative integer.

    Returns:
    bool: True if the number is prime, False otherwise.

    Examples:
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(29)
    True
    >>> is_prime(100)
    False
    >>> is_prime(97)
    True

    Notes:
    - The function uses the square root to reduce the number of checks.
    - Negative numbers and numbers less than 2 are not considered prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

# Set the range of numbers that we'd like to get prime numbers for
num_range = range(1,70)
prime_numbers = list(filter(is_prime, num_range))
print(f"The prime numbers between 1 and 70 are:\n{prime_numbers}")
