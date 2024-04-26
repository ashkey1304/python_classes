# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    first_num = int(input("Enter the number:"))
    second_num = int(input("Enter the number:"))
    result = first_num + second_num
    print("sum of the two number:", result)
except:
    raise TypeError('The input is not numerical.')