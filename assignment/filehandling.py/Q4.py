# Write a Python program to read last n lines of a file.
a = open('hello.txt', 'r')
b = a.readline(5)
print(b)
a.close()