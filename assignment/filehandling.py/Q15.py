# Write a Python program to read a random line from a file.
import random
a = open('file2.txt', 'r')
b = a.read().splitlines()
random.choice(b)
print(b)