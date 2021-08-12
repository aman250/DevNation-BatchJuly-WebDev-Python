def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3


# User Defined Values
num1=int(input("Enter the First number:_ "))
num2=int(input("Enter the Second number:_ "))
num3=int(input("Enter the Third number:_ "))
print("the maximum value is ",maximum(num1,num2,num3))

