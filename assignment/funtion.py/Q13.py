# Write a Python function that prints out the first n rows of Pascal's triangle.
def tringal(n):
    for i in range(7):
            a = 1
    for j in range(0 , i + 1):
          print(a , end=" ")
          a = a*(i-j)//(j+1)
    print()