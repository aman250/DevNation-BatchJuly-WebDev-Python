
no1 = int(input('enter your no: '))
no2 = int(input('enter your no: '))
character = input('enter your operators: ')
if character == '-':
    print('result ' +str(no1 - no2))
elif character == '*':
    print('result ' +str(no1 * no2))
elif character == '//':
    print('result ' + str(no1 // no2))
elif character == '+':
    print('result ' +str(no1 + no2))
else:
    print('invalid')







