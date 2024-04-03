temp = int(input("Enter the temperature : "))
unit = int(input("1 for c-f and 2 for f-c:"))
if unit == 1:
    f = (9*(temp/5)) + 32
    print(f)
elif unit == 2:
    c = 5*((temp - 32)/9)
    print(c)