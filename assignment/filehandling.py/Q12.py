# Write a Python program to write a list to a file.
list_1 = ['apple', 'banana', 'cherry']
with open('hello.txt', 'w') as h:
    for item in list_1:
        h.wite(item + '\n')
h.close()