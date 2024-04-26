# Write a Python program to assess if a file is closed or not.
a = open('hello.txt', 'r')
print(a.close)
a.close()
print(a.close)