def average(numbers):
    return sum(numbers)/len(numbers)


def even_odd(num):
    if num % 2 == 0:
        print("Result is even")
    else:
        print("result is Odd")


nums = list(map(float, input("Enter three number you want to add; space separated? ").split(" ")))

average_num = average(nums)
print(f"Average of the list: {average_num}")

even_odd(average_num)