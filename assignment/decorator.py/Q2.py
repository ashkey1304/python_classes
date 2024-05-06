# Write a  Python program to create a decorator function to measure the execution time of a function.
import time
def my_decorator(fumc):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        fumc(*args, **kwargs)
        end_time = time.time()
        result = end_time - start_time
        print(result)
        return wrapper
@my_decorator
def my_funtion(a,b):
    print(a + b)
x = int(input("Enter the num:"))
y = int(input("Enter the num:"))