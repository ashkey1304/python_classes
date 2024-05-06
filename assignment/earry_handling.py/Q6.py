# Write a  Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
try:
    the_inuput = int(input("Enter the index:"))
    num = [1,2,3,4,5,6,7,8,9]
    if the_inuput in num:
        print("it's in the list")
except:
    raise IndexError('Error: Index out of range.')
