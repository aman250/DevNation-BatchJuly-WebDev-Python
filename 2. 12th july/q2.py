held=int(input('enter classes held:'))
taken=int(input('enter classes taken:'))
attendance=taken/held*100

print("attendance is= "+str(attendance)+" percent.")
if attendance<75:
    print("You are not allowed to sit in exam")
else:
    print("You are allowed to sit in exam")

    


