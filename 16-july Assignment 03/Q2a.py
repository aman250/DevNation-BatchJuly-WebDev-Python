patternRows = int(input("Enter the Number of Rows: "))
print(patternRows)
i = 1
while i <= patternRows:
    j = patternRows
    while j >= i:
        print("*", end=" ")
        j -= 1
    print()
    i += 1