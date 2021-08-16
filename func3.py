# function to check whether average is even or odd

def avg_even_or_odd(avg):
    print('Average of given list is: ',round(avg))
    if (avg % 2 == 0):
        print(avg,' is an even number')
    else:
        print(avg, 'is an odd number')

# function to calculate average of list
def calc_avg(nums):
    avg=sum(nums)/len(nums)
    return avg_even_or_odd(round(avg))



### Function call
calc_avg([3,5,9,9])
