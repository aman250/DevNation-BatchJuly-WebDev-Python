#question no 2 (a) part
a = int(input("enter your first value"))
b = int(input("enter your second value"))
sum = a+b
print(sum)

#question no 2 (b and c) part

first_number = input('enter first number:')

second_number = input('enter second number:')

#take operand as input
operand = input('enter operand:')


#question no 2 (c) part
if operand == '+':
    result = int(first_number)+int(second_number)
    print("addition of "+ str (first_number) +'and '+ str(second_number)  + 'is' + str(result))

elif operand == '-':
     result = int(first_number) - int(second_number)
     print("addition  of" + str(first_number) + 'and' +str(second_number) + 'is' + str(result))

elif operand == '*':
    result = int(first_number) * int(second_number)
    print("addition of" + str(first_number) + 'and'+ str(second_number) + 'is'+ str(result))

elif operand =='/':
    result = int(first_number) / int(second_number)
    print("addition of" + str(first_number)+'and'+ str(second_number)+'is'+str(result))