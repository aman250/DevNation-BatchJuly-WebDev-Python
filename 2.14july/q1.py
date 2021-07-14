print("_________________________CALCULATOR_______________________")
num1=input("Enter the 1st Number:_ ")
num2=input("Enter the 2nd Number ")
op=input("chose one operator: +,-,*,/,%")

if op=="+":
    print("the addition of two numbers "+num1+" and "+num2+" is "+str(int(num1)+int(num2)))
elif op=="-":
    print("the subtraction of two numbers " + num1 + " and " + num2 + " is " + str(int(num1) - int(num2)))
elif op=="*":
    print("the multiplication of two numbers " + num1 + " and " + num2 + " is " + str(int(num1) * int(num2)))
elif op=="/":
    print("the division of two numbers " + num1 + " and " + num2 + " is " + str(int(num1) / int(num2)))
else:
    print("the percentage of two numbers " + num1 + " and " + num2 + " is " + str(int(num1) % int(num2)))
