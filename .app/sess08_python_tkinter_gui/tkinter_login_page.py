# Python GUI script to demonstrate a Tkinter login window

# Import modules
import tkinter as tk
from tkinter import messagebox

# Define a function to authenticate the user
def login():
    #pass
    username = entry_username
    password = entry_password

    # Ensure that user has filled in their username/password
    if username.get().strip() =="" or password.get().strip() == "":
        tk.messagebox.showerror("Error", "Please enter both username and password")
        return

    if username.get().strip() == 'admin' and password.get().strip() =='pas$1':
        tk.messagebox.showinfo("Login Successful", "Welcome back, Admin")
    else:
        tk.messagebox.showerror("Login failed", "Incorrect username or password. Please try again")
# Function to toggle password visibility
def toggle_password():
    #pass
    if show_password.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

# Create the main window
root = tk.Tk()
root.title("Login Screen")
root.geometry("320x240")
root.resizable(width=False, height=False)

# Create a centered frame
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Labels
label_username = tk.Label(frame,text="Username: *")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")

label_password = tk.Label(frame,text="Password: *")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

#Entry fields
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=10, pady=10)

entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)


# Checkbox for showing/hiding the password
show_password = tk.BooleanVar()
checkbox_show_password = tk.Checkbutton(frame, text="Show Password",variable=show_password, command=toggle_password)
checkbox_show_password.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Login button
button_login = tk.Button(frame, text="Login", command=login)
button_login.grid(row=3, columnspan=2, pady=20)

# Run the application
root.mainloop()
