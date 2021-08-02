
first_number = input('Enter first number: ')

second_number = input('Enter second number: ')

operand = input('Enter operand: ')

if operand == '+':
    result = int(first_number)+int(second_number)
    print("Addion of " + str(first_number) + ' and '+ str(second_number)+' is ' + str(result))

elif operand == '-':
    result = int(first_number) - int(second_number)
    print("Substraction of " + str(first_number) + ' and ' + str(second_number) + ' is ' + str(result))

elif operand == '*':
    result = int(first_number) * int(second_number)
    print("Multiplication of" + str(first_number) + ' and ' + str(second_number) + ' is ' + str(result))

elif operand == '/':
    result = int(first_number) / int(second_number)
    print("Division of " + str(first_number) + ' and ' + str(second_number) + ' is ' + str(result))

elif operand == '%':
    result = int(first_number) % int(second_number)
    print("percentage of " + str(first_number) + ' and ' + str(second_number) + ' is ' + str(result))

else:
    print('Please enter a valid operand...!')