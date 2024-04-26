# Write a Python program to read a file line by line store it into a variable.
a = open('hello.txt', 'r')
b = a.readlines()
print(b)
for i in b:
    print(i)