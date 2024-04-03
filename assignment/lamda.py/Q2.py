#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def multiply(n):
    return lambda x : x * n
result = multiply(2)
print("double of 15:", result(15))
result = multiply(3)
print("triple of 15:", result(15))
result = multiply(4)
print("quadruple of 15:", result(15))
result = multiply(5)
print("quintuple of 15:", result(15))
