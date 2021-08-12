""""
    Takes a list of integers as argument and 
    return its average
"""
def list_avg(my_list):
    sum = 0
    for i in my_list:
        sum += i
    return sum/len(my_list)

""""
    Takes an integer as argument and 
    return True if it is Even and False if it is Odd
"""
def even_odd_checker(num):
    if num % 2 == 0:
        return True
    else:
        return False
"""
    tests the above functions
"""
def main():
    sample_list = [4,6,5,7,8]
    print('The list is ' + str(sample_list))
    avg = list_avg(sample_list)
    print('and its average is:'+ str(avg))
    if even_odd_checker(avg):    
        print('The calculated average is Even')
    else:
        print('The calculated average is Odd')

if __name__ == "__main__":
    main()