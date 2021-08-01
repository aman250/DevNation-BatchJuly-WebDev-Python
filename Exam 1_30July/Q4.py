#Q4 Python Exam

print("\n\t\t\t\t\t\t Factorial of\n\t\t\t\t\t\t  Any Number\n\n")
user_fact_number=int(input("\t\tEnter the Number To Find The factorial:_ \n\t\t\t\t"))
display=user_fact_number
result_factorial=1
for fact_number in range(user_fact_number,0,-1):
        result_factorial *=fact_number

print("\n\t\tFactorial Result Of The Inputted Number ",display," Is \"",result_factorial,"\"\n\n\t\t\t\t\t\t Code By Haseeb Rehman\n\n\t\t\t\t\t\t\t\t******** ")