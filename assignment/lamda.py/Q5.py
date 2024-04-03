#Write a  Python program to filter a list of integers using Lambda.
whole_num = [1,2,3,4,5,6,7,8,9,10]
even_num = list(filter(lambda x : x %2 == 0, whole_num))
print("Even number:", even_num)
odd_num = list(filter(lambda x: x %2 != 0, whole_num))
print("Odd number:", odd_num)