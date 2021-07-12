classes_held = int(input("Enter the total numbers of classes held:"))
classes_attended = int(input("Enter the number of classes attended by the student:"))
percentage = (classes_attended/classes_held) * 100

if 75 <= percentage <= 100:
    print("Percentage:",percentage)
    print('Status: Allowed to sit in  exam')
elif 0 <= percentage < 75:
    print("Percentage:", percentage)
    print('Status: Not allowed to sit in  exam')
else:
    print("Invalid Input...")
