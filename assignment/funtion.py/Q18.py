# Write a Python program to execute a string containing Python code.
py_code = 'print("Hello World")'
code = """
def mutiply(x,y):
    return x*y
print('Multiply of 2 and 3 is: ', mutiply(2, 3))
"""
exec(py_code)
exec(code)