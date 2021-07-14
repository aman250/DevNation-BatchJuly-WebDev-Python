print('A.')
for i in range(1, 5):
    for j in range(i):
        print('*', end="")
    print()
print()

print('B.')

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

print('C.')

num = 4
for n in range(num):
    for space in range(n):
        print(" ",end="")
    for ones in range(num-n):
        print('1',end="")
        if ones != num-n-1:
            print('0',end="")
    print()