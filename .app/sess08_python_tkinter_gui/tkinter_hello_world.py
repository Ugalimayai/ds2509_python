#Python GUI with a label and button to display a message on the screen once button is clicked

import tkinter as tk

# set the root component
root = tk.Tk()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y positions to center the window/GUI
x = (screen_width - 640) // 2
y = (screen_height - 640) // 2

# Set the dimensions of the window
root.geometry("640x480+{}+{}".format(x,y))

# Create a label and its context(text) and font size
label = tk.Label(root, text="Hello World!", font=("Arial", 25), fg="blue", bg="black")
label.pack()

# Function to toggle the text on the above label
def toggle_text():
 if label['text'] == "Hello World!":
     label['text'] = "Bye World!"
 else:
     label['text'] = "Hello World!"


# Create a button with its content and font size
button = tk.Button(root, text="Toggle Text", command=toggle_text, font=("Arial", 25), fg="white", bg="skyblue")
button.pack()

# Run the application
root.mainloop()