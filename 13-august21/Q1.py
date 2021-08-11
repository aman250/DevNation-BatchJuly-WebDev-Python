def maxnumber(num1,num2,num3) :
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    elif num2>num3:
        return num2
    else:
        return num3

max=maxnumber(5000,1000,140000)
print("Maximum number is : " +str(max))