# Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    length_list = len(num_list)
    print("Length of the list; ", length_list)
except AttributeError:
    print("AttributeError: the attribute does not exist.")