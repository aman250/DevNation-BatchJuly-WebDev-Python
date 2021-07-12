class_held = int(input("Enter No. of Classes held: "))
class_attend = int(input("Enter No. of Classes Attend: "))
percentage = (class_attend/class_held)*100
print(percentage)
if percentage >= 75:
  print("The student is allowed to sit in Exam.")
else:
  print("The student is not allowed to sit in Exam.")