x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
op = str(input("Enter the operator for the operation you want to perform:"))

if op == '+':
    print("The sum of the numbers you entered is " + str(x + y))
elif op == '-':
    print("The difference of the numbers you entered is " + str(x - y))
elif op == '*':
    print("The product of the numbers you entered is " + str(x * y))
elif op == '/':
    print("The quotient of the numbers you entered is " + str(x / y))
elif op == '%':
    print("The remainder of division of the numbers you entered is " + str(x % y))
else:
    print("Invalid Operator...")

