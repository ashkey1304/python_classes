# Write a Python program to create a decorator to convert the return value of a function to a specified data type.
def my_decorater(fumc):
    def wapper(*args, **kwargs):
        fumc(*args, **kwargs)
        return wapper
@my_decorater
def add_ing(x, y):
    x + y 
num1 = int(input("Enter the nomber:"))
num2 = int(input("Enter the number:"))
add_ing()