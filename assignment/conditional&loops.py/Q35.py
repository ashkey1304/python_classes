# Write a Python program that checks whether a string represents an integer or not.
text_string = input("Enter the string: ")
text = text_string.strip()
if len(text) < 1:
    print("Input a valid text")
else:
    if all (text[0] in "+-") and all(text[i] in "0123456789" for i in range(1, len(text))):
        print("The string is an integer.")
    else: print("Ten string is not an integer.")
    