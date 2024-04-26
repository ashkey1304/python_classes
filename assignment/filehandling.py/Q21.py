# Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.
import string
n = []
a = open("file2.txt", "w")
alph_abet = string.ascii_letters
litt_ers = [alph_abet[i:i + n] +"\n" for i in range(0, len(alph_abet), n)]
a.writelines(litt_ers)
n(3)