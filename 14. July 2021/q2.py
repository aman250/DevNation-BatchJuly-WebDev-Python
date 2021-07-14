import math
print('A.')
for i in range(1, 5):
    for j in range(i):
        print('*', end="")
    print()
print()

print('B.')
n= int(input("Enter number of rows"))
rows = math.ceil(row/2)
for i in range(rows):
    print(" " * (rows-i) + "*" * (i*2+1))
for j in range(1, rows):
    print(" " * (j+1) + (((rows-j)*2-1) * '*'))

print('C.')
num=4
for i in range(num,0,-1):
    for space in range(num-i):
        print(" ",end="")
    for n in range(1, 2*i):
        print(n%2, end="")
    print()
'''
###Part B

#rows = int(input("Enter the odd number of rows you want"))
rows = 5
n = rows//2 + 1
for i in range(n):
    for j in range(n - i):
        print(" ", end="")
    for k in range((2*i)+1):
        print('*', end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(n-i+1):
        print(" ", end="")
    for k in range((i*2)-1):
        print("*", end="")
    print()

## Part B with while loop


a = n+1
i = 0
while a>0:
    j=0
    k=0
    while j<n-i:
        print(" ", end="")
        j += 1
    while k < (2*i)-1:
        print("*", end="")
        k+=1
    i+=1
    a -= 1

    print()

a= n-1
i = 0
while a > 0:
    j = 0
    k = 0
    while j < i+1:
        print(" ", end="")
        j += 1
    while k < (2*a) - 1:
        print("*", end="")
        k += 1
    i += 1
    a -= 1

    print()
###print('C.')
num = 4
for n in range(num):
    for space in range(n):
        print(" ",end="")
    for ones in range(num-n):
        print('1',end="")
        if ones != num-n-1:
            print('0',end="")
    print()
'''
