num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
result=0
operator=input('enter operator(+,-,*,/ or %):')

if operator=='+':
    result=num1+num2
    print("result="+str(result))
elif operator=='-':
    result=num1-num2
    print("result="+str(result))
elif operator=='*':
    result=num1*num2
    print("result="+str(result))
elif operator=='/':
    result=num1/num2
    print("result="+str(result))
elif operator=='%':
    result=num1%num2
    print("result="+str(result))
else:
    print('please enter correct operator!')


