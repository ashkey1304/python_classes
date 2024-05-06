# Write a  Python program to create a decorator that logs the arguments and return value of a function.
def my_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f'{args}')
    return wrapper
@my_decorator
def my_funtion(a,b):
    print(a+b)
x = int(input("Enter the a number:"))
y = int(input("Enter the a number: "))
my_funtion(x,y)