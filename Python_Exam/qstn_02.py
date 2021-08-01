print("Both numbers must be integers to perform the calculations on the basis of operator entered")
#User Defined Input
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operator=input("Enter an operator:")
#Conditional operator Statements
if(operator=="+"):
    add=num1+num2
    print("The addition of two numbers is:"+str(add))
elif(operator=="-"):
    sub=num1-num2
    print("The subtraction of two numbers is:"+str(sub))
elif(operator=="*"):
    mul=num1*num2
    print("The multiplication of two numbers is:"+str(mul))
elif(operator=="/"):
    div=num1/num2
    print("The division of two numbers is:"+str(div))
elif(operator=="%"):
    mod=num1%num2
    print("The modulus of two numbers is:"+str(mod))
else:
    print("Invalid operator entered")