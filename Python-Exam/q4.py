

### Calculating Factorial
num = int(input('Enter number whose factorial needs to be determined: '))

if num == 0 or num == 1:
    print(num,'! = ',1)

else:
    fact = 1
    for i in range(1 , num+1):
        fact *= i
    print(num,'! =', fact)



