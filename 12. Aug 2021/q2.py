def addition(numbers):
    return sum(numbers)


nums = list(map(float, input("Enter three number you want to add; space separated? ").split(" ")))

print(f"Sum of above numbers: {addition(nums)}")