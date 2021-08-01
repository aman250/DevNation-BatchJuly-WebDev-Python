#Question no.2:

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
op = input("Enter an operator:")

if op == "+":
    print("you have entered ", op ,"so the answer is= ", (num1 + num2))
elif op == "-":
    print("you have entered ", op, "so the answer is= ", (num1 - num2))
elif op == "*":
    print("you have entered ", op, "so the answer is= ", (num1 * num2))
elif op == "/":
    print("you have entered ", op, "so the answer is= ", (num1 / num2))
elif op == "%":
    print("you have entered ", op, "so the answer is= ", (num1 % num2))
else:
    print("you've entered an invalid operator!")