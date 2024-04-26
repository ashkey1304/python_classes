# Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
sum = num_1 + num_2
if sum in range (15, 21):
    print("20")
else:
    print(sum)