# Write a  Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
word_string = input("Enter the string:")
if len(word_string) < 2:
    print('empty String')
else:
    print(word_string[:2] + word_string[:-2])