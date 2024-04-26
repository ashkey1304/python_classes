# Write a  Python program to detect the number of local variables declared in a function.
def abc():
    x = 3
    y = 4

print(abc.__code__.co_nlocals)