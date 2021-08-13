def maxNumber(num1,num2, num3):
    if(num1 > num2) and (num1 > num3):
        print("Num1 is Maximum:", num1)
    elif (num2 > num1) and (num2 > num3):
        print("Num2 is Maximum:", num2)
    else:
        print("Num3 is Maximum:", num3)

# function call
maxNumber(5, 4, 6)
