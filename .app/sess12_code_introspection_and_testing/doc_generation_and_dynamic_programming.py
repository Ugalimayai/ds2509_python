# Python script to demonstrate function documentation generation and dynamic programming using introspection


def add(a, b):
    """
    Calculates the sum of two numbers
    :param a(int,float): The first number to be summed/added
    :param b(int,float): The second number to be summed/added:
    :returns:
       int,float: The sum of two numbers. The return type depends on the type of input

    Example:
       >>> add(1,2)
       3
       >>> add(3,4.5)
       7.5
       >>> add(2.5,3.1)
       5.6

    Notes:
         - The function can handle both integers and floating-point numbers.
         - The result type will match the type of the inputs. For example, adding an integer to a float will yield a float.
         - If either `a` or `b` is a non-numeric type, a `TypeError` will be raised.

     Raises:
         TypeError: If `a` or `b` is not an integer or float.
    """
    return a + b

print(f"The 'doc-string' (Documentation String) for the add function given below:\n{add.__doc__}")

# Function to accept an arithmetic operator and two numbers to perform the operation on

def perform_operation(operation, x, y):
    """
    Performs a basic arithmetic operation ('add', 'subtract', 'multiply', or 'divide') on two numbers.

    :param operation: A string indicating the operation to perform.
                      Accepted values are 'add', 'subtract', 'multiply', and 'divide' (case-insensitive).
    :type operation: str
    :param x: The first numeric operand.
    :type x: int or float
    :param y: The second numeric operand.
    :type y: int or float

    :return: The result of applying the specified operation to the operands.
    :rtype: int or float

    :raises ValueError: If the operation is not one of the supported options.
    :raises ZeroDivisionError: If a division by zero is attempted.

    :example:
        >>> perform_operation('add', 2, 3)
        5
        >>> perform_operation('SUBTRACT', 10, 4)
        6
        >>> perform_operation('multiply', 2.5, 4)
        10.0
        >>> perform_operation('divide', 9, 3)
        3.0

    :notes:
        - The operation string is case-insensitive.
        - Both integer and floating-point numbers are supported.
        - If `y` is 0 and the operation is 'divide', a ZeroDivisionError will be raised.
    """
    if operation.lower() == 'add':
        return add(x, y)
    elif operation.lower() == 'subtract':
        return x - y
    elif operation.lower() == 'multiply':
        return x * y
    elif operation.lower() == 'divide':
        return x / y
    else:
        raise ValueError(f"Operation'{operation}' is not supported!\n"
                         f"Please use 'add', 'subtract', 'multiply' or 'divide' instead.")

# Use global(s) to dynamically access and execute the 'perform_operation' function
operation, num1, num2  = 'add',5,3
print(f"The result of the operation: {operation} on {num1} and {num2} is:\n{perform_operation(operation, num1, num2)}")

# Get values from the user
operation = input(f"Please enter the arithmetic operation: "
                  f"\n'add' for addition, "
                  f"\n'subtract' for subtraction, "
                  f"\n'multiply' for multiplication, "
                  f"\n'divide' for division: \n")

num1 = int(input("Please enter the first number to be used in the calculation:\n"))
num2 = int(input("Please enter the second number to be used in the calculation:\n"))

# Perform the operation and display the result
print(f"Result of operation:{operation} on {num1} and {num2} is:\n"
      f"{perform_operation(operation, num1, num2)}")



