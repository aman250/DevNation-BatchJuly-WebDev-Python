# Q3

flag = 'q'

nums = []
sum = 0
average = 0
product = 1

while flag == 'q':
    num = input('Enter another number:')
    nums.append(int(num))
    flag = input(
        'Enter "q" to continue entering number and anything else to quit: ')

for num in nums:
    sum = sum+num
    product = product*num

average = sum/len(nums)
print('list=', nums)
print('average=', average)
print('product=', product)
