my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
sum = 0

for item in my_list:
    sum += item

average = sum/len(my_list)
print(f"The average of the list given is: {average}")
print(f"\nList before insertion : {my_list}")
print("Inserting 65 on index 4...")
my_list.insert(4,65)
print(f"\nList after insertion : {my_list}")
