#Write a Python program to get the Fibonacci series between 0 and 50.
a = 0 
b = 1
for i in range(0, 51):
    print(a)
    a = b
    b = a + b
    