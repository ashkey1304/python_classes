# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    file_name = open('file', 'r')
    a = file_name.read()
    print(a)
    file_name.close()
except FileNotFoundError:
    print("Error: File  not found.")