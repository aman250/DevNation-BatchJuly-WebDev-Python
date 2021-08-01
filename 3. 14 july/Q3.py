add=0
counting= 0
while True:
    print("enter the number(enter q to exit)")
    n=input()
    if n=="q":
        break
    n=int(n)
    counting = counting + 1
    add = add + n
print("average of number is :", add / counting)