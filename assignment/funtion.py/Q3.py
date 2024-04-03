#Write a Python function to multiply all the numbers in a list
def abc(a):
    m = 1
    for i in a:
        m *= i
    return m
l = [1,2,3,4,5,6]
r = abc(l)
print(r)