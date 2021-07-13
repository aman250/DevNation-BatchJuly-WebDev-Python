classesheld = int(input("How many classes are held : "))
classesattend = int(input("How many classes have attended : "))
percent = int((classesattend / classesheld) * 100)
print(percent)
if percent >= 75 and percent <= 100:
    print("you are allowed to sit in the exams")
elif percent < 75:
    print("you are not allowed to sit in the exams")
