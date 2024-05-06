# Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    dividend = float(input("Input the dividend: "))
    divisor = float(input("Input the divisor:"))
    division = dividend / divisor
    print("Result: ", division)
except:
    raise ArithmeticError("Error: ArithemeticError.")