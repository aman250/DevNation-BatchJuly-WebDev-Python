# write a program that inputs integers and operands to perform the operations
frist_number= input("ENTER YOUR FRIST INTEGER: ")
second_number= input("ENTER YOUR SCEOND INTEGER: ")
operator= input("ENTER THE OPERATOR YOU WANT: ")

if operator=='+':
    SUM= int(frist_number) + int(second_number)
    print("SUM IS: " + str(SUM))
elif operator=='-':
    SUBTRACTION = int(frist_number) - int(second_number)
    print("SUBTRACTION IS: " + str(SUBTRACTION))
elif operator=='*':
    PRODUCT = int(frist_number) * int(second_number)
    print("PRODUCT IS: " + str(PRODUCT))
elif operator=='/':
    DIVISION = int(frist_number) / int(second_number)
    print("DIVISION IS: " + str(DIVISION))
elif operator=='%':
    REMAINDER = int(frist_number) % int(second_number)
    print("REMAINDER IS: " + str(REMAINDER))
else:
    print("YOU ENTER INVALID OPERATOR")