# Python script to demonstrate how to handle multiple exceptions

try: # Code that may raise errors
    num_list = [3,5,8]
    # Try to print a number at an invalid index
    print(f"Value at index 7 is: {num_list[7]}")

    # Other possible exceptions
    num_list + 5 # TypeError as you cannot sum an int with a list
    num_list.remove(4) # ValueError as the list has no item 4

    # Attempt integer division by zero
    quotient = 12/0
except IndexError:
    print("Error: The index you tried to access is out of range.")
except TypeError:
    print("Error: Sorry, you can't add an integer and a list.")
except ValueError:
    print("Error: Sorry, the list does not contain number '4'.")
except ZeroDivisionError:
    print("Error: Attempted integer division by zero. Change the denominator to non-zero value.")
