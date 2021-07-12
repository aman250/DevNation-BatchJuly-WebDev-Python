#Program to calculate the percentage of attendence of a student

#Take input from User
total_classes=input("Enter total number of classes that are held:")
attended_classes=input("Enter number of attended classes:")
percentage=float(attended_classes)/float(total_classes)*100

#Display percentage of classes attend
print("The percentage of attended classes is:"+str(percentage)+"%")

#Check whether student is allowed to sit in exam or not
if percentage>=75:
    print("Your attendence percentage is " + str(percentage) + " so you are allowed to sit in exam")
else:
    print("Your attendence percentage is" + str(percentage) + "so you are not allowed to sit in  exam")






