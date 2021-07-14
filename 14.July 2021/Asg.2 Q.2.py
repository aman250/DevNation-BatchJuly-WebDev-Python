class_held = int(input("Number of classes held?: "))
class_attended = int(input("Number of classes attended?: "))

attendance = round((class_attended/class_held)*100, 2)

print(f"Percentage of attendance: {attendance}")
if attendance > 75:
    print("Allowed to sit in the exam!!")
elif attendance < 75:
    print("Attendance short: Not allowed to sit in the Exam")
else:
    print("Invalid inputs. Try again!!")