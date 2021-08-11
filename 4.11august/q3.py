def avg(array):
    s = sum(array)
    average = s / len(array)
    return average


def ev(num):
    if num % 2 == 0:
        print("Number is even!")
    else:
        print("Number is odd!")


a = avg([1, 2, 3, 4, 5])
print("Average = ", str(a))
ev(a)
