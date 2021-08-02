print("My calculator")
first_number = int(input("enter first number :"))
second_number = int(input("please enter second number :"))
print("operations type")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
print("% for percentage")
operator = input("please select any one of above option")
result = 0
if operator == "+":
    result = first_number + second_number
if operator == "-":
    result = first_number - second_number
if operator == "*":
    result = first_number * second_number
if operator == "/":
    result = first_number / second_number
if operator == "%":
    result = first_number / second_number * 100
print(f"Result: {result}")
