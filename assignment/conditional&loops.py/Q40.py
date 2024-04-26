# Write a Python program to find the median of three values.
first_num = int(input("Enter the first number:"))
second_nun = int(input("Enter the second number:"))
third_num = int(input("Enter the third number:"))
if first_num > second_nun and first_num < third_num:
    mid_num = first_num
elif second_nun > third_num and second_nun < first_num:
    mid_num = second_nun
else:
    if first_num > third_num and second_nun < third_num:
        mid_num = second_nun
    else:
        mid_num = third_num
print("The mible number is ", mid_num)