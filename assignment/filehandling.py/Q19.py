#  Write a Python program to extract characters from various text files and puts them into a list.
import glob
list_1 = []
b = open("hello.txt", 'r')
a = glob.glob("hello.txt")
c = list_1.append(b.read())
print(list_1)