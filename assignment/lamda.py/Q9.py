#Write a python program to check weather a given string is a number or not using lambda.
check_startswith = lambda string, char: string.startswith(char)

# Test the lambda function
input_string = input("Enter a string: ")
input_char = input("Enter a character: ")

if check_startswith(input_string, input_char):
    print(f"The string '{input_string}' starts with the character '{input_char}'.")
else:
    print(f"The string '{input_string}' does not start with the character '{input_char}'.")