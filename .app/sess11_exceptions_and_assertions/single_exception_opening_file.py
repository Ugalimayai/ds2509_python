# Python script that demonstrates handling an exception raised when the user tries to open a non-existing file.

try: #write code that may raise an exception here
    file = open('non-existent.bin', 'rb')
    content = file.read()
    print(f"File contents are:\n{content}")
except FileNotFoundError: # Handle the file error here
    print("Error, sorry the file was not found.\nPlease check the path and file name & ensure you have access permissions, then try again.")
finally:
    if 'file' in locals():
        file.close()