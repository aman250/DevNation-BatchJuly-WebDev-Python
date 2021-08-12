def average(no):
    return sum(no) / len(no)


no = [1, 2, 3, 4, 10]
print(average(no)
      )


def check(average):
    if average(no) % 2 == 0:
        print('even')
    else:
        print('odd')

check(average)
