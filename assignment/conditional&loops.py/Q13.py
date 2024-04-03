#Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers tha are divisible by 5 in a comma separated sequence.
item = []
num = [x for x in input().split(",")]
for n in num:
    x = int(n, 2)
    if not x % 5:
        item.append(x)
print(item)