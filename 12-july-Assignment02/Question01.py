
numberOne = input("Enter First Number:")
print(numberOne)
numberTwo = input("Enter Second Number:")
print(numberTwo)
oneOperator = input("Enter any operator:")
print(oneOperator)
if oneOperator == "+":
    print("The Result is " + str (int(numberOne) + int(numberTwo)))

elif oneOperator == "-":
    print("The Result is " + str(int(numberOne) - int(numberTwo)))

elif oneOperator == "*":
    print("The Result is " + str(int(numberOne) * int(numberTwo)))

elif oneOperator == "/":
    print("The Result is " + str(int(numberOne) / int(numberTwo)))

elif oneOperator == "%":
    print("The Result is " + str(int(numberOne) / int(numberTwo)))
else:
    print("invalid operator")
