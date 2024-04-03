#Write a Python program to remove all elements from a given set.
s = {1,2,3,4,5}
f = frozenset(s)
f.add(6)
print(f)