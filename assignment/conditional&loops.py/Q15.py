# Write a Python program to check the validity of passwords input by users.
import re


password_input = input("Enter the password: ")
x = True
while x:
    if (len(password_input) < 6 or len(password_input) > 12):
        break
    elif not re.search("[a-z]", password_input):
        break
    elif not re.search ("[0-9]", password_input):
        break
    elif not re.search("[A-Z]", password_input):
        break
    elif not re.reach("[!@#$%^&*()_+]", password_input):
        break
    else:
        print("Valid Passward")
        x = False
        break
    if x:
        print("Not a Valid Passward")