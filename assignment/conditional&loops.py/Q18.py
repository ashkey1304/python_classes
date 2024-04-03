#Write a Python program to print the alphabet pattern 'D'.
for row in range(7):
    for col in range(5):
        if (col == 0) or ((row == 0 or row == 6) and (1 = col = 5)) or ((row != 0) and (row != 6)) 
            print('*', end="")