def a(array):
    addition = sum(array)
    avg = addition/len(array)
    return avg


def b(num):
    if num % 2 == 0:
        print("your number is even")
    else:
        print("your number is odd")


c=a([1, 2, 3, 4, 5])
print("Average =", str(c))
b(c)
