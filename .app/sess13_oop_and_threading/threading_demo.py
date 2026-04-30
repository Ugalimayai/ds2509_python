# Python file to demonstrate creating multiple threads to display numbers and letters

#import the required modules
import threading

# Function to run in a separate threading
def print_numbers():
    for n in range(1,1000):
        print(f"From thread1: n={n}")

# Function to run in another separate thread
def print_letters():
    for letter in 'abcdefghijklmnopqrstuvwxyz'*10:
        print(f"From thread2: letter={letter}")

# Create thread objects and start them
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()
