# Write a Python program to combine each line from first file with the corresponding line in second file.
with open('hello.txt' ) as a, open('file2.txt') as f:
    for l1 , l2 in zip(a, f):
        print(l1 + l2)