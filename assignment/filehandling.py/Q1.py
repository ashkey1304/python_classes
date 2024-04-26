# Write a Python program to read an entire text file.
a = open('hello.txt', 'r')
b = a.read()
print(b)
a.close()