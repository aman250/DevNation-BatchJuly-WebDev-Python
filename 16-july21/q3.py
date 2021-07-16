import numpy

num_lst=[]
n=input("press q to quit: ")
while n!="q":
    ele=int(input("please enter your integer: "))
    num_lst.append(ele)
    n = input("press q to quit: ")

avg=sum(num_lst)/len(num_lst)
print("Your average is: " + str(avg))
product=numpy.prod(num_lst)
print("your product is: " + str(product))