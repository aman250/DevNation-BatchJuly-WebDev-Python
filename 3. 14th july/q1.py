num = int(input('enter number to take factorial of:'))
if num < 0:
    print('negative number has no factorial')
elif(num == 0):
    print('factorial=1')
else:
    i = num-1
    while i > 1:
        num = num*i
        i = i-1
    print('factorial=', num)
