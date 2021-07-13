number1 =input("enter first number")
number2 =input("enter second number")
operator =input("enter operator")
if operator=="+":
    result= int(number1)+int(number2)
    print(result)
elif operator == "-":
    result= int(number1)-int(number2)
    print(result)
elif operator=="*":
    result= int(number1)*int(number2)
    print(result)
elif operator=="/":
    result= int(number1)/int(number2)
    print(result)
elif operator=="%":
    result= int(number1)%int(number2)
    print(result)
else:
    print("invalid operator")