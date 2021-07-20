# a: for rows
print('Half pyramid pattern')
for rows in range (0,4):
    #for columns
    for col in range(0,rows+1):
        print('*', end='')
    print('\n')


# b: diamond shape
print('Diamond Shape:')
rows=4
for i in range (rows):
    print(" " * (rows-i)+ " *"
*(i+1))
for j in range (rows-1):
    print(" " * (j+2) +
" * "(rows-1-j))


#c
print ('Binary pattern')

rows=4
for i in range(rows , 0 , -1):
    for j in range(1,i+1):
        print(j%2, end=' ')
    print()
