# Write a Python program to remove newline characters from a file.
a = open('file2.txt', 'r')
b = a.readlines()
r = a.rstrip(['/n'])
print(r)