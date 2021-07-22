total_classes = int(input('Enter total number of classes: '))

classes_attended = int(input('Enter number of classes attended: '))

attendance = int((classes_attended / total_classes) * 100)

print(str(attendance) + '%')

if attendance < 75:
    print('You are not allowed sit in exams')
else:
    print('You are allowed to sit in exams')
