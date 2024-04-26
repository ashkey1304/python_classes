# Write a Python program to check if a triangle is equilateral, isosceles or scalene.
lenght_1 = int(input("First side: "))
lenght_2 = int(input("Scond side: "))
length_3 = int(input("Third side: "))
if lenght_1 == lenght_2 == length_3 :
    print("Equilateral triangle")
elif lenght_1 == lenght_2 or lenght_2 == length_3 or length_3 == lenght_1:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")