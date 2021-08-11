def list_average(list):
    avg=0
    for i in list:
        avg+=i
    return avg/(len(list))
def check_res(avg):
    if avg%2==0:
        return "Even"
    else:
        return "odd"

list=[3,2,1,4,6,1,2,10]
avg=list_average(list)
print("average of list is" , avg)
print("the list is" ,check_res(avg))

