#python script to demonstrate the scope of local and global variables

# declare a global variable
global_var = 5

#define a function to display the value passed to it
def display_value(value):
    print(f"The value passed is: {value}")

#call the display_value() func and pass in the global var
display_value(global_var)

def random_function():
    random_variable = "Hello" #random variable is only accessible within random_function only
    return random_variable

#call  the display_value() function and pass in the random variable
display_value(random_variable)


