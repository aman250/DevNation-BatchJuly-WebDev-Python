num = int(input('Enter number to take factorial of:'))

factorial=1

if num < 0:
    print('negative number has no factorial')
elif num==0:
    print('Factorial of ',num,' is=',1)
else:
    for x in range(1,num+1):
        factorial*=x
    print('Factorial of ',num,' is=',factorial)    
