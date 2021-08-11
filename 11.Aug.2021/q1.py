

### function to calculate max number.

def find_max(num1,num2,num3):
    if (num1>num2) and (num1>num3):
        print('Max number is: '+ str(num1))
    elif (num2 > num1) and (num2 > num3):
        print('Max number is: ' + str(num2))
    else:
        print('Max number is: ' + str(num3))


# Function call
find_max(3,0,1)