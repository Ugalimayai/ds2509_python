# Python GUI app to accept url from the user and validate it using a regular expression (regex)

# import modules
import re
import tkinter as tk
from tkinter import messagebox, END

# Function to validate the URL
def validate_url():
    """
    Validate the format of a URL entered in a GUI input field.

    This function retrieves the URL from a GUI entry widget, trims any
    surrounding whitespace, and checks if the URL matches a basic pattern
    for HTTP or HTTPS URLs. If the URL is empty, it shows an error message.
    If the URL matches the pattern, it shows a success message; otherwise,
    it shows an error message.

    Returns:
        None: The function does not return a value. It uses message boxes
              to display the result of the validation.
    """
    url = entry_url.get()
    if not url:
        tk.messagebox.showerror("Missing URL",
                                "Please enter the URL to be validated!")
        return
    pattern = r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if re.match(pattern, url):
        tk.messagebox.showinfo("Valid URL",
                               "The URL entered is valid!")
    else:
        tk.messagebox.showerror("Invalid URL",
                                "Sorry, the URL entered is not valid!")

def clear_text():
    entry_url.delete(0, END)
    entry_url.focus()
# set up the GUI
root = tk.Tk()
root.title("Validate URL")

#Label(s)
label_url = tk.Label(root, text="URL Address:")
label_url.grid(row=0, column=0, padx=10, pady=5)

#Entry Field
entry_url = tk.Entry(root)
entry_url.grid(row=0, column=1, padx=10, pady=5)

# Buttons
button_validate= tk.Button(root, text="Validate URL", command=validate_url)
button_validate.grid(row=1, column=0, padx=10, pady=5)

button_clear = tk.Button(root, text="Clear URL", command=clear_text)
button_clear.grid(row=1, column=1, padx=10, pady=5)

# run the application
root.mainloop()

