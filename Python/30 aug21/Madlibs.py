import random
def guessNum(range):
  randomNum = random.randint(1,range)
  guess =0
  while guess != randomNum:
    guess = int(input("Enter number between 1 and " + str(range) + ": " ))
    if guess > randomNum:
      print("Sorry! Try again, your guess id too high")
    elif guess< randomNum:
      print("Sorry! Try again, your guess is too low")
  print("Yay! you have guessed the number " + str(randomNum) + " correctly.")


def computer_guess(range):
  low = 1
  high = range
  feedback = ""
  while feedback != "c":
    if low != high:
      guess = random.randint(low,high)
    else:
      guess = low 
    feedback = input("Is the number " + str(guess) + " is too high (h), or too low (l) or is it correct (c): ")
    if feedback == "h":
      high = guess - 1
    elif feedback == "l":
      low = guess + 1
  print("Pheewwww The number is guessed correctly!")
computer_guess(10)