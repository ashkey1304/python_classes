#Write a Python function that checks whether a passed string is a palindrome or not.
def string(p):
    return p == p[::-1]
w = input("Enter the word: ")
r = string(w)
print(r)