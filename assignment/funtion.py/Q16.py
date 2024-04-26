#Write a Python function to create and print a list where the values are th9e squares of numbers between 1 and 30.
def square():
    l = list()
    for i in range(1, 31):
        l.append(i ** 2)
    print(l)
square()