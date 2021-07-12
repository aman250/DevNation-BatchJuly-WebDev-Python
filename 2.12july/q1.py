num1= input("Enter first number:")
num2= input("Enter second number:")
ch= input("Enter an operator:")
if ch == '+':
    result = int(num1) + int(num2)
elif ch == '-':
    result = int(num1) - int(num2)
elif ch == '*':
    result = int(num1) * int(num2)
elif ch == '/':
    result = int(num1) / int(num2)
elif ch == '%':
    result = int(num1) % int(num2)
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)

