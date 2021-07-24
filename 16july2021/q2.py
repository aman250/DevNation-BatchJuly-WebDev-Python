for rows in range(0,4):
    #for columns
    for col in range(0,rows+1):
        print('*',end='')
    print("\n")

    #Diamond shape
rows = 4
for i in range (rows):
   print(" " * (rows-i) + " *" *(i+1))
for j in range  (rows-1):
    print(" " * (j+2) + " *"*(rows-1-j))

       #Question 2(c)
print("\nQ2 part c\n ")
my_list=[1,0,1,0,1,0,1]
k=0
for i in range(len(my_list),-1,-2):
    print(" " *(k),end='')
    for j in range(i):
        print(my_list[j],end='')
    print('')

    k+=1
    print(' ')
