numberOfrows = int(input("Enter Number of rows: "))
print(numberOfrows)
for i in range (1,numberOfrows + 1):
    print(" "*(numberOfrows - i) + "* "*i)
for i in range(numberOfrows - 1, 0,-1):
    print(" "*(numberOfrows-i) + "* "*i)
