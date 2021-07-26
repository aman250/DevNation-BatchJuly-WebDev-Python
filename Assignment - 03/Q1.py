# Factorial

num = int(input('Enter the number to know the factorial: '))

fact = 1

if num == 0 or num == 1:
    print(1)
elif num < 0:
    print('Factorial does not exist')
else:
    for i in range(1, num + 1):
        fact = fact * i
    print('fact of ', num, 'is', fact)
