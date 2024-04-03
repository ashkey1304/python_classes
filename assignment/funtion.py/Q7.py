#Write a Python function that accepts a string and counts the number of upper and lower case letters.
def string(w):
    upper_case = 0
    lower_case = 0
    for c in w:
        if c.islower():
            lower_case += 1
        elif c.isupper():
            upper_case += 1
    return upper_case, lower_case
e = input("Enter the word: ")
s = string(e)
print(s)
