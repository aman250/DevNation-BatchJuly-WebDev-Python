print("My name is __________.")
name = "shahid" 
turns = 10
for x in range(10):
  print("You have", turns, "turns.")
  guess = input("Enter a word of your choice: ")
  if(guess==name):
    print("My name is "+ name)
    print("Congrats! You have won.")
    break
  if(x==9):
    print("OOPS! Game Over.")
  turns-=1