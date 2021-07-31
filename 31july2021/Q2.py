num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operator = input("Enter Operator: ")
if operator == "+":
  sum = num1 + num2
elif operator == "-":
  sum = num1 - num2
elif operator == "/":
  sum = num1 / num2
else:
  sum = num1 * num2
print(sum)