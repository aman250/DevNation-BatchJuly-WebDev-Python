a = int(input("number of classes held;"))
b = int(input("number of classes attended;"))
percentage = (b/a)*100

if percentage>=75:
    print("the students is allowed to sit in the exam hall")
else:
     print("the students is not allowed to sit in the exam hall")