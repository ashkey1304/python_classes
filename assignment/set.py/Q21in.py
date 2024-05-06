# Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
list_word = ['red', 'green', 'red', 'blue', 'red', 'red', 'green']
word_set = set(list_word)
word_count = word_set.count(list_word)
print(word_count)