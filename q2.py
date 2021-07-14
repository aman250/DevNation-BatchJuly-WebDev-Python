classes = int(input('enter your classes'))
attendance = int(input('enter your attendace'))
percantage = attendance/classes*100
print(float(percantage))
if percantage >= 75:
    print('A student will  be allowed to sit in an exam')
else:
    print('A student will not be allowed to sit in an exam')



