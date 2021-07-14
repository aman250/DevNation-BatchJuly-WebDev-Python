user_quit=""
user_list=[]
while user_quit!="q":
    num=int(input("Enter the interger value"))
    user_list.append(num)
    user_quit=input("You want to quit:")

product=1
addition=0
#to calculate addition of all numbers for average
for i in range(0,len(user_list)):
    addition+=user_list[i]
print("Average of user inputs number is",addition/len(user_list))

#product of all user inputed numbers
for i in range(0,len(user_list)):
    product*=user_list[i]

print("Product value is ",product)