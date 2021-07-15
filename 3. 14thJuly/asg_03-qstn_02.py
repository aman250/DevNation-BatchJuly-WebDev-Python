#program to display Patters
#-----------------PART "A"

print("\n---------------part a--------------------")
i=1
while i<=4:
    j=1
    while j<=i:
        #here i will use end= funtion that is use to place a space after * instead of a newline
        print("*",end='')
        j=j+1
    print()
    i+=1

#-----------------PART "B"

print("\n---------------part b--------------------")
n=5
for i in range(0,n,2):
    print(" "*(n-i)+" *"*(i+1))

for j in range(n-2,-1,-3):
    print(" "*(n-j)+" *"*(j+1))


#-----------------PART "C"

print("\n---------------part c--------------------")
lst=[1,0,1,0,1,0,1]
space=0
for i in range(len(lst),-1,-2):
    print(" " *(space),end="")
    for j in range(i):
        print(lst[j],end="")
    space=space+1
    print(" ")
