#Write a  Python program to square and cube every number in a given list of integers using Lambda.
list_int = [1,2,3,4,5,6,7,8,9,10]
squ_num = (lambda x : x**2, list_int)
print("Square of all integer:",squ_num)
cube_num = (lambda x : x ** 3, list_int)
print("cube of all intreger:", cube_num)