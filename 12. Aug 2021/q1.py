def max_number(num1):
    return max(i for i in num1)


numbers = map(float, input("Enter three number you want would like to know the maximum by space separated? ")
              .split(" "))
print(f"Maximum number: {max_number(numbers)}")

