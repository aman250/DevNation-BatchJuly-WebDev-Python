def average(lst):
    sum=0
    for i in lst:
        sum+=i
    av=sum/len(lst)
    return av

def EvenOrOdd(num):
    if(num%2==0):
        return 'Even'
    elif(num%2==1):
        return 'Odd'
    else:
        return 'in decimal, so it is neither Even nor Odd!'

lst=[2,2,3,4,5]

print('Average of list is ',EvenOrOdd(average(lst)))

