# Write a Python program to append text to a file and display the text.
a = open('hello.txt', 'a+')
a.write('bye!!')
a.seek(0)
c = a.read()
print(c)
a.close()