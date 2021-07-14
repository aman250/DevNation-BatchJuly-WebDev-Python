a=input("Total number of classes held:")
b=input("Number of classes attended:")
r= (int(b) * 100) / int(a)
print("total attendance percentage:", r, "%")
if r > 75 :
    print("you're allowed to sit in the class")
else:
    print("You're not allowed to sit in the class")