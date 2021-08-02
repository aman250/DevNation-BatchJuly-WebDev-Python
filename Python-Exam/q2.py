


#### Take tow inputs from user
first_number = input('Enter first number: ')

second_number = input('Enter second number: ')

### Take operand as input
operand = input('Enter operand: ')



### print the result according to operand entered by user
if operand == '+':
    result = int(first_number)+int(second_number)
    print("Addion of " + str(first_number) + ' and '+ str(second_number)+' is ' + str(result))

elif operand == '-':
    result = int(first_number) - int(second_number)
    print("Subtraction of " + str(first_number) + ' and ' + str(second_number) + ' is ' + str(result))

elif operand == '*':
    result = int(first_number) * int(second_number)
    print("Multiplication of " + str(first_number) + ' and ' + str(second_number) + ' is ' + str(result))

elif operand == '/':
    result = int(first_number) / int(second_number)
    print("Division of " + str(first_number) + ' and ' + str(second_number) + ' is ' + str(result))

elif operand == '%':
    result = int(first_number) % int(second_number)
    print("Mode of " + str(first_number) + ' and ' + str(second_number) + ' is ' + str(result))

else:
    print('Please enter a valid operand...!')


