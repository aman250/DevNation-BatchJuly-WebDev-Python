def calculates_power(bn,pn): #bn=BaseNumber pn=PowerNumber
    power=1
    for i in range(pn):
        power *=bn
    return power


print("\n\t\t\t\t\t******************************************  ****************************************** \n\t\t\t\t\t"
                  "                                          Q1                                          \n\t\t\t\t\t"
                  "******************************************  ******************************************")
base_number=int(input("\n\t\t\t\t\tEnter a \"Base\" number:_ "))
power_number=int(input("\n\t\t\t\t\tEnter a \"Power\" number:_ "))
print("\n\t\t\t\t\tresult of base number",base_number,"and power number",power_number,"is:_ ",calculates_power(base_number,power_number))
