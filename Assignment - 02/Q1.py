first_number = input('Enter first Number: ')
second_number = input('Enter second Number: ')

operator = input('Enter an operator: ')

if operator == '+':
    result = int(first_number) + int(second_number)
    print(result)
elif operator == '-':
    result = int(first_number) - int(second_number)
    print(result)
elif operator == '*':
    result = int(first_number) * int(second_number)
    print(result)
elif operator == '/':
    result = int(first_number) / int(second_number)
    print(result)
elif operator == '%':
    result = int(first_number) % int(second_number)
    print(result)
else:
    print('Invalid Operator')
