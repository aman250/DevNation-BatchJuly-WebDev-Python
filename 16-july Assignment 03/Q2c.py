numberOfrows = 4

for i in range(numberOfrows, 0,-1):

    for j in range(numberOfrows - i):
        print(" ",end="")
    for k in range(1, 2*i):
        print(k%2, end="")
    print()