#part (a)
n = int(input('Enter number of rows : '))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1


#part (b)

rows = int(input("Enter the number of rows: "))
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
k = rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")





   #part(c)
n = int(input('Enter number of rows : '))

i = 1
while i <= n:
    j = n
    while j >= i:
        print("10", end=" ")
        j -= 1
    print()
    i += 1