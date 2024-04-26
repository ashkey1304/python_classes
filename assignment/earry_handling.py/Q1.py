# Write a  Python program to handle a ZeroDivisionError exception when dividing a number by zero.
num_enter = int(input("Enter the number:"))
try:
    result = num_enter / 0
    print("Ans.",result)
except ZeroDivisionError:
    print("Not allowed")