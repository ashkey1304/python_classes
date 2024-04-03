#Write a Python program to sort a list of tuples using Lambda.
list = [('English', 88), ('Sciience', 90), ('Maths', 97), ('Social Science', 82)]
list.sort(key=lambda x : x[1])
print("sorted_list:", list)