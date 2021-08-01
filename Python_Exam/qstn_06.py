print("\n\t\t\t\t--------Program to create and display values of tuple---------")

#tuple creation
my_tuple=("10","20","30","40","50","60")
print("The tuple is="+str(my_tuple))

#access the value of tuple from specific position
print("\nThe value at index 3 is:"+(my_tuple[3]))

print("\nThe values of tuple are:")
#display all the values of tuple using for loop
for i in range(len(my_tuple)):
    print(my_tuple[i])