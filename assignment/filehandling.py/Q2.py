# Write a Python program to read first n lines of a file.
a = open('hello.txt', 'r')
for i in range(4):
    b = a.readline()
    print(b)
a.close()