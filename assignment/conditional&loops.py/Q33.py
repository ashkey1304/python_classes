# Write a Python program to convert a month name to a number of days.
month_name =input("Enter name of the month: ")
if month_name == "February":
    print("No. of days: 28/29")
elif month_name == ['January', 'March', 'May','July', 'Aug', 'September', 'October', 'December']:
    print("No. of days : 31")
elif month_name == ['April', 'June', 'September', 'November']:
    print("No. of days : 30")
else:
    print("month name is not corret.")