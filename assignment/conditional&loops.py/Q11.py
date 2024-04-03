#Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*
a = int(input("Enter the number:"))
b = int(input("Enter the number"))
c =[[ 0 for col in range(b)] for row in range (a)]
for row in range(a):
    for col in range(b):
        c[row][col] = row*col
print(c)