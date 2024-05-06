# Write a  Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input. 
try:
    input_num = int(input("Input a number: "))
    print("You entered:", input_num)
except KeyboardInterrupt:
    print("input canceled by the user.")