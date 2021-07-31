def fact(n):
    result = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            result *= i
        return result


num = int(input("Enter the number you want to calculate factorial?: "))

if num >= 0:
    print(f"{num}! = {fact(num)}")
else:
    print("Invalid input!!")