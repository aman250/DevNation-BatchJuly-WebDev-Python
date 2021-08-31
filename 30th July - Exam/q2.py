num1 = int(input('Enter first number:'))
num2 = int(input('Enter 2nd number:'))
operator = input('enter operator(+,-,*,/ or %):')
result = 0
if operator == '+':
    result = num1+num2
    print("result="+str(result))
elif operator == '-':
    result = num1-num2
    print("result="+str(result))
elif operator == '*':
    result = num1*num2
    print("result="+str(result))
elif operator == '/':
    result = num1/num2
    print("result="+str(result))
elif operator == '%':
    result = num1 % num2
    print("result="+str(result))
else:
    print('please enter correct operator!')

print('Answer is=', result)
