def lst_average(lst):
    avg=0
    for i in lst:
        avg+=i
    return avg/(len(lst))
def check_res(avg):
    if avg%2==0:
        return "Even"
    else:
        return "Odd"

#built in list
lst=[3,2,1,4,6,1,2,10]
avg=lst_average(lst)   #here the avg comes from the avg checking function
print("average of list is ",avg)
print("the list is ",check_res(avg))
