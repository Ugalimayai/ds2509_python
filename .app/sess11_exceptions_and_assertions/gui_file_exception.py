# Python file to demonstrate handling multiple exceptions in a GUI program
# to read and display the file contents

# import the required modules
import tkinter as tk
from tkinter import filedialog, messagebox
import sys

# Function to process the file and calculate the average
def process_file():
    """
        Read a file specified in the GUI entry widget, extract numeric values,
        and compute their average.
        The function retrieves the file path from a text entry field, reads the
        file content, and attempts to parse numbers (comma- or space-separated).
        It then calculates the average of the extracted values and displays the
        result in a label widget.
        Error handling:
            - FileNotFoundError: If the specified file does not exist.
            - PermissionError: If the file cannot be accessed due to permission issues.
            - ValueError: If the file is empty or contains no valid numeric data.
            - ZeroDivisionError: If division by zero occurs (unlikely with current logic).
            - OSError: For other file-related errors.
            - Exception: Catches any unexpected errors.
        Side Effects:
            Updates the global `result_label` widget with either the computed
            average or an appropriate error message.
        Returns:
            None
        """
    file_name = entry.get()
    result_label.config(text=f"") # Clear the previous result

    try:
        with open(file_name, 'r') as file:
            content = file.read().strip()

            if not content: # When the file is empty
                raise ValueError("The file was not found.")

            # Replace commas with spaces, the split
            values = content.replace(',', ' ').split()

            # convert to float or int
            numbers = [float(value) for value in values]

            if len(numbers) == 0:
                raise ValueError("No valid numbers found!")

            average = sum(numbers) / len(numbers)

    except FileNotFoundError:
        # Handle the error when the file doesn't exist
        result_label.config(text=f"Error: File {file_name} not found!Kindly check path and try again.")

    except PermissionError:
        # Handle the error when the program doesn't have the access rights to the file
        result_label.config(text=f"Error: Permission denied while accessing {file_name}.")

    except (ValueError, ZeroDivisionError):
        # Handle invalid integer/values or division by '0'
        result_label.config(text=f"Error: File must contain a non-zero integer.")

    except OSError as os_error:
        # Handle other file related errors(e.g. permission errors)
        result_label.config(text=f"Error: File access error:\n{os_error}")

    # handle all other unexpected errors
    except:
        result_label.config(text=f"Unexpected error occurred. Please try again.")
        # in a full-fledged app, you can log the errors into file here
    else:
        result_label.config(text=f"Success! The average score is {average:.2f}.")


# Function to open a file dialog and populate the entry field
def browse_file():
    """
    Open a file selection dialog and populate the entry widget with the chosen file path.

    This function launches a file dialog allowing the user to select a file.
    If a file is selected, its path is inserted into the entry widget, replacing
    any existing content.

    Side Effects:
        Modifies the global `entry` widget by clearing its current content and
        inserting the selected file path.

    Returns:
        None
    """
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"),("All Files","*.*")])
    if file_path:
        entry.delete(0,tk.END) # Clear the current entry
        entry.insert(0,file_path)

# Create the main tkinter window
root = tk.Tk()
root.title('File Reader - Average Score Calculator')
root.geometry('480x180') # set the window size

# Create and pack the GUI elements
tk.Label(root, text='Enter path to scores file or browse').pack(padx=10, pady=10)

# Frame for entry and browse button
entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=10)

#Text entry for file name
entry = tk.Entry(entry_frame, width=45)
entry.pack(side=tk.LEFT, padx=5)

# Browse button
tk.Button(entry_frame, text='Browse', command=browse_file).pack(side=tk.LEFT)

# Process button to trigger file reading
tk.Button(root, text='Process File', command=process_file).pack(pady=10)

# Label to display the results or error messages
result_label = tk.Label(root, text='', wraplength=450)
result_label.pack(pady=10)

# start the application
root.mainloop()