#Write a python program to extract year, month, date and time using lambda.
from datetime import datetime

current_date = datetime.now()

year = lambda: current_date.year
month = lambda: current_date.month
date = lambda: current_date.day
time = lambda: current_date.strftime("%H:%M:%S")

print("Current year: ", year())
print("Current month: ", month())
print("Current date: ", date())
print("Current time: ", time())