def max1(num1, num2, num3):
    m = num1
    if num1 > num2 and num1 > num3:
        m = num1
    elif num2 > num1 and num2 > num3:
        m = num2
    else:
        m = num3
    return m
print("max is ",max1(3,4,5))
