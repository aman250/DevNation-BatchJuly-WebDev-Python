# Q2

first_number = input('Enter a first number: ')
second_number = input('Enter a second number: ')

operand = input('Enter operand: ')

if operand == '+':
    result = int(first_number) + int(second_number)
    print("Addition of " + str(first_number) + ' and ' + str(second_number) + ' is ' + str(result))

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
    print('Please enter a valid operand!!!')
