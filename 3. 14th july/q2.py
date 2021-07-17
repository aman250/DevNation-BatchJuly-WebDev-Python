
# part a
print('Part a:')
i = 1
while i <= 4:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1


# part b
print('Part b:')
n = 4
k = 3
for i in range(0, n):

    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")

n = 4
for j in range(n-1):
    print(" " * j + " *"*(n-1-j))


# c
print('Part c:')

rows = 7
indent_counter = 0
for i in range(rows, 0, -2):
    for j in range(1, i+1):
        print(j % 2, end='')
    print('')
    for i in range(indent_counter+1):
        print(' ', end='')
    indent_counter += 1
