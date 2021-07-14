numbers = input("Enter two numbers, separated by space, you want to operate?: ").split(" ")
num1 = float(numbers[0])
num2 = float(numbers[1])

operator = input("Enter one of the following operators ( +, -, *, /, or %)? ")

if operator == "+":
    print(f"Result of sum: {num1+num2}")
elif operator == "-":
    print(f"Result of subtraction: {num1-num2}")
elif operator == "*":
    print(f"Result of Multiplication: {num1*num2}")
elif operator == "/":
    print(f"Result of division: {num1/num2}")
elif operator == "%":
    print(f"Result of remainder: {num1%num2}")
else:
    print("Invalid operator")