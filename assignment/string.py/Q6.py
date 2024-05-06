# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
add_word = input("Ente The Word:")
if len(add_word) < 3:
    print('short')
if add_word.endswith('ing'):
    print()
