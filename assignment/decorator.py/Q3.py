# Write a Python program to create a decorator to convert the return value of a function to a specified data type.
def my_decorater(fumc):
    def wapper(*args, **kwargs):
        fumc(*args, **kwargs)
        return wapper
@my_decorater
