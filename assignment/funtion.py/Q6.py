#Write a Python function to check whether a number falls within a given range
def range(a):
    if a in (3, 9):
        print("%s is in the range" % str(a))
    else:
         print("the number is outside the give rage.")
e = int(input("Enter the number: "))
range(e)