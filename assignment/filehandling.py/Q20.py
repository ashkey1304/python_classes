# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string, os
if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_letters:
    with open(letter + "hello,txt", "w") as a:
        a.writelines(letter)