# Write a  Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
first_word = input("Enter the string:")
second_word = input("Enter the string:")
new_word1 = first_word[:2] + second_word[:-2]
new_word2 = first_word[:-2] + second_word[:2]
print('new word:', new_word1)
print('new word:', new_word2)