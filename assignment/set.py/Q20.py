#Write a Python program to remove the intersection of a second set with a first set.
s = {1,2,3,4,5}
s1 = {4,5,6,7,8}
i = s.intersection(s1)
for i in s & s1:
    s.remove(i)
    print(s)