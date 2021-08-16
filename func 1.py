### calculating max value.

def find_max(num1,num2,num3):
    if (num1>num2) and (num1>num3):
        print('Max number is: '+ str(num1))
    elif (num2 > num1) and (num2 > num3):
        print('Max number is: ' + str(num2))
    else:
        print('Max number is: ' + str(num3))


# now its time to call Function
find_max(9,6,7)