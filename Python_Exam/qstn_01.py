print("-------------------Method 1 Using for loop-----------------------")
print("SQUARE SHAPE")

#For loop
#outer loop for rows
for row in range(0,8):
    #inner loop for columns
    for col in range(0,15):
        if(row==0 or row==7):
            print("-", end=" ")
        elif(col==0 or col==14):
            print("|", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n\t\t-------------------Method 2 Using print statements------------------------")
print("-----------------------------")
print("|                           |")
print("|                           |")
print("|                           |")
print("|                           |")
print("|                           |")
print("|                           |")
print("-----------------------------")
