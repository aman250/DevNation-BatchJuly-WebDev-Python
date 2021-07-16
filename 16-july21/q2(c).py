rows=4
for i in range(rows):
    for space in range(i):
        print(" ", end=" ")
    for ones in range(rows-i):
        print("1", end=" ")
        if ones !=rows-i-1:
            print("0", end=" ")
    print()
