a = input("enter a number")
b = input("enter a number")
c = input("enter a operator")
if c == '+':
    print(int(a) + int(b))
elif c == '-':
    print(int(a) - int(b))
elif c == '*':
    print(int(a) * int(b))
elif c == '/':
    print(int(a) / int(b))
else:
    print("you should enter only a number for calculation")