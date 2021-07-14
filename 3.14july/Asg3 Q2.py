#--------------Q3 A ----------------
print("Q2 part a\n")
i=1
j=1

for i in range(5):
    for j in range(i):
        print("*", end='')
    print('')

#----------------Q3 B ---------------
print("\nQ2 part b\n")
stars=5
for i in range(0,stars,2):
    print(" "*(stars-i)+" *"*(i+1))
for i in range(stars-2,-1,-3):
    print(" "*(stars-i)+" *"*(i+1))

#----------------Q3 C ---------------
print("\nQ2 part c\n ")
my_list=[1,0,1,0,1,0,1]
for i in range(len(my_list),-1,-2):
    for j in range(i):
        print(my_list[j],end='')
    print('')

