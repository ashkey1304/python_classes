#Write a Python program to check if two given sets have no elements in common.
s = {1,2,3,4}
s1 = {5,6,7,8} 
if s.intersection(s1):
    print('yes')
else:
    print('no')