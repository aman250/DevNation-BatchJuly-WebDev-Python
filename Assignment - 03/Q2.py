print('Part A')
for rows in range(0, 4):
    # for columns
    for col in range(0, rows + 1):
        print('*', end=' ')
    print('\n')

print('Part B')
rows = 4
for i in range(rows):
    print(" " * (rows - i) + " *" * (i + 1))
for j in range(rows - 1):
    print(" " * (j + 2) + " *" * (rows - 1 - j))

print('Part C')
rows = 4
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j % 2, end=' ')
    print()
