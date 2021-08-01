# Q2: Write a program that does the following
# 1. Take two Integer inputs from the user.
# 2. Take input from the user for the operand.
# 3. Do the following calculation according to the operand and integer values that has been
# inputted from the user.

integer = float(input('enter your no 1: '))
integer2 = float(input('enter your no 2: '))
operand = input('operation: ')
if operand == '+':
    print((integer + integer2))
elif operand == '-':
    print(integer - integer2)
elif operand == '/':
    print(integer / integer2)
elif operand == '*':
    print(integer * integer2)
elif operand == '%':
    print(integer2 % integer)
