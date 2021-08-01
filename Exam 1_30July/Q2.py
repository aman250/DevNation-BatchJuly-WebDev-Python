#Q2 Python Exam
#Q2 part 1
print("\n\t\t\tQ2 part 1:\n")
print("Enter two Integers Input:")  #this statement prompt a user to input only integer
inpt1=int(input("1st input:_  "))  # inpt1 is the first input from user
inpt2=int(input("\n2nd input:_  "))  # inpt1 is the second input from user

#Q2 part 2
print("\n\t\t\tQ2 part 2:\n")
operand=input("Enter the operand:_  ") #operand is taking signs input from user

#Q2 part 3
print("\n\t\t\tQ2 part 3:\n")
if operand=="+":
    print("Answer is ",inpt1+inpt2,"\n\n\t\t\t\t\t\t Code By Haseeb Rehman\n\n\t\t\t\t\t\t\t\t******** ")
elif operand=="-":
    print("Answer is ",inpt1-inpt2,"\n\n\t\t\t\t\t\t Code By Haseeb Rehman\n\n\t\t\t\t\t\t\t\t******** ")
elif operand=="*":
    print("Answer is ",inpt1*inpt2,"\n\n\t\t\t\t\t\t Code By Haseeb Rehman\n\n\t\t\t\t\t\t\t\t******** ")
elif operand=="/":
    print("Answer is ",inpt1/inpt2,"\n\n\t\t\t\t\t\t Code By Haseeb Rehman\n\n\t\t\t\t\t\t\t\t******** ")
elif operand=="%":
    print("Answer is ",inpt1%inpt2,"\n\n\t\t\t\t\t\t Code By Haseeb Rehman\n\n\t\t\t\t\t\t\t\t******** ")
else:
    print("Invalid operand","\n\n\t\t\t\t\t\t Code By Haseeb Rehman\n\n\t\t\t\t\t\t\t\t******** ")