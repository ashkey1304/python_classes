#Write a python program that accepts a sequence of lines as input and prints the lines as output.
empty_list=[]
while True:
    l = input ()
    if l:
        empty_list.append(l.upper())
    else:
        break;
for l in empty_list:
    print(l)