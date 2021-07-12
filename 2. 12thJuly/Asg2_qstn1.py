#program to built calculator

num1=input("Enter first number:")
num2=input("Enter second number:")
operator=input("Enter an operator:")
#Addition
if operator=="+":
    result=float(num1)+float(num2)
    print("The addition of two numbers is:"+str(result))

#subtraction
elif operator=="-":
    result = float(num1) - float(num2)
    print("The subtraction of two numbers is:" + str(result))

#Multiplication
elif operator=="*":
    result = float(num1) * float(num2)
    print("The multiplication of two numbers is:" + str(result))

#Division
elif operator=="/":
    result = float(num1) / float(num2)
    print("The division of two numbers is:" + str(result))

#Modulus
elif operator=="%":
    result = float(num1) % float(num2)
    print("The modulus of two numbers is:" + str(result))

#Invalid Result
else:
    print("Invalid operator entered!")
