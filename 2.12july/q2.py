num1=input("Total number of classes held:")
num2=input("Number of classes attended:")
result= (int(num2) * 100) / int(num1)
print("total attendance percentage:", result, "%")
if result > 75 :
    print("you're allowed to sit in the class")
else:
    print("You're not allowed to sit in the class")
