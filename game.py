from random import randint

def print1():
  print("-------------------------------------------")

def gamble():
  tries = 0
  game_num = randint(1,100)
  for i in range(8):
    tries += 1
    num = int(input("Enter your guess: "))
    if num > 100 or num < 1:
      print("Number is out play.")
      print1()
    elif num < game_num:
      print("Number is wrong, the number is also lower than the secret number.")
      print1()
    elif num > game_num:
      print("Number is wrong, the number is also greater then the secret number")
      print1()
    elif num == game_num:
      print(f"Congratuations you got the right one. It took you {i + 1} times.")
      print1()
      break
    else:
      print("You are wrong, try again.")
      print1()
    if tries == 8:
      print(f"You were wrong 8 times the secret number was {game_num}.")
      print1()

