#Write a Python program to print the even numbers from a given list.
def even(l):
    null_list = []
    for n in l:
        if n %2 == 0:
            null_list.append(n)
    return null_list
list = [1,2,3,4,5,6,7,8,9,10]
e = even(list)
print(e)