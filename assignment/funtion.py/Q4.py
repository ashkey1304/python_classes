#Write a Python program to reverse a string.
def abc(a):
    r = "".join(reversed(a))
    print("output: ", r)
W = input("Enter the word: ")
abc(W)