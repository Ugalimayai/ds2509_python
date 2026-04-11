# Python script to create a simple tkinter calculator for addition, multiplication
# ,subtraction, and division.

#import required modules
import tkinter as tk
from tkinter import ttk, messagebox #ttk is for the combobox

# define a function to read in the values from the user
def calc():
    # get the numbers and operation from the entry field and combobox
    first_number = entry_first.get()
    second_number = entry_second.get()
    operation = entry_operation.get()

    #check if any of the above fields are empty
    if not first_number.strip() or not second_number.strip() or not operation.strip():
        messagebox.showerror(title="Missing Values or Operation", message="Please enter all values and select the arithmetic operations")

        return #stop further method execution
    try:
        #convert the vales from input fields to numbers
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        messagebox.showerror("Invalid Values", "Please enter valid numeric values for the first & second number")
        return

    # check for division by zero
    if operation == "/" and second_number == 0:
        messagebox.showerror("Divide by Zero Error", "Cannot divide by zero(0). Please enter a non-zero denominator")
        return

    # Define the arithmetic operator mappings
    # operations = \
    #     {
    #     "+": first_number + second_number,
    #     "-": first_number - second_number,
    #     "x": first_number * second_number,
    #     "/": first_number / second_number,
    #     }

    match operation:
        case '+':
            result_first = first_number + second_number
        case "x":
            result_first = first_number * second_number

        case "/":
            result_first = first_number / second_number
        case "-":
            result_first = first_number - second_number
        case _:
            messagebox.showerror("Invalid Operation", "Please enter a valid operation")
            return
    label_answer.config(text=f"Result: {result_first}")
    # check whether the operation is valid and show the result
    # if operation in operations:
    #     result = operations[operation]
    #     label_answer.config(text=f"result:\t{result}")
    # else:
    #     messagebox.showerror("Invalid Operation", "Please enter a valid operation")


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("640x480")
root.resizable(width=False, height=True)

#Create a centered frame
frame = tk.Frame(root)
frame.place(relx=.5, rely=.5, anchor="center")

#label widgets
label_first = tk.Label(frame, text="First Number:")
label_first.grid(row=0, column=0, padx=10, pady=10, sticky="e")

label_operation = tk.Label(frame, text="Operation(+,-,x, or /)")
label_operation.grid(row=1, column=0, padx=10, pady=10, sticky="e")

label_second = tk.Label(frame, text="Second Number:")
label_second.grid(row=2, column=0, padx=10, pady=10, sticky="e")

label_answer = tk.Label(frame, text="Answer/Result:")
label_answer.grid(row=3, column=0, padx=10, pady=10, sticky="e")

#specify the width for the input/entry widgets
input_width = 25 # same width for all input controls/widgets

# Entry widgets and combobox
entry_first = tk.Entry(frame, width=input_width)
entry_first.grid(row=0, column=1, padx=10, pady=10)
entry_first.insert(0,"Enter first number") #placeholder text
entry_first.focus() # set the focus/blinking cursor or insertion point on this control

# dropdown combobox for the desired arithmetic operation
operation_choices = ['+', '-', 'x', '/']
entry_operation = ttk.Combobox(frame, values=operation_choices, state="readonly", width=input_width-3)
entry_operation.grid(row=1, column=1, padx=10, pady=10)
entry_operation.set("Select Operation") # Default value for the combobox/dropdown list

entry_second = tk.Entry(frame, width=input_width)
entry_second.grid(row=2, column=1, padx=10, pady=10)
entry_second.insert(0,"Enter second number")

#Submit/Calculate button
button_calc = tk.Button(frame, text="Calculate", command=calc)
button_calc.grid(row=4, columnspan=2, padx=10, pady=10)

#run the application
root.mainloop()