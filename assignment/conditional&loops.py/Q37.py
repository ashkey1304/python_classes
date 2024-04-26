# Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
month_name = input("Name of the month: ")
date = int(input("Enter the Date: "))
if month_name in ('Jan', 'Feb','Dec'):
    print("Winter")
elif month_name in ('Mar', 'Apr', 'May'):
    print("Spring")
elif month_name in ('Jun', 'July', 'Aug'):
    print("Summer")
elif month_name in ('Sep', 'Oct', 'Nov'):
    print("Autumn")
else:
    print("invalid.")
if (month_name == 'Mar') and (date > 19):
    print("spring")
elif (month_name == 'Jun') and (date > 20):
    print("Summer")
elif (month_name == 'Sep') and (date > 21):
    print("Autumn")
else:
    print("ivalid")