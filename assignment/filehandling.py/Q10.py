# Write a Python program to count the frequency of words in a file.
from collections import counter
def word_count(hello.txt):
    with open(hello.txt) as h:
        return counter(h.read().split())
print(word_count("hello.txt"))