# Write a Python program to calculate a dog's age in dog years.
'''Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.'''
input_age = int(input("Enter the dogs in human age: "))
if input_age <= 2:
    print(input_age * 10.5)
else:
    print((21 + (input_age - 2) * 4))
     