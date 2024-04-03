#Write a Python function to check whether a number is "Perfect" or not.
def perfect_num(n):
    if n < 1:
        return False
    d = 0 
    for i in range (1, int(n)):
        if n %i == 0:
            d += i
    return d == n
print(perfect_num(6))
print(perfect_num(3))
print(perfect_num(28))