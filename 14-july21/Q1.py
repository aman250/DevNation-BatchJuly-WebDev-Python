First_number=input("enter your first number: ")
Second_number=input("enter your second number: ")
Operator=input("enter the operator you want: ")
if Operator=='+':
    sum=int(First_number)+int(Second_number)
    print("sum is: " + str(sum))
elif Operator=='-':
    subtraction=int(First_number)-int(Second_number)
    print("subtraction is: " + str(subtraction))
elif Operator=='*':
    product=int(First_number)*int(Second_number)
    print("product is: " + str(product))
elif Operator=='/':
    division=int(First_number)/int(Second_number)
    print("division is: " + str(division))
elif Operator=='%':
    Remainder=int(First_number)%int(Second_number)
    print("Remainder is: " + str(Remainder))
else:
    print("invalid operator")