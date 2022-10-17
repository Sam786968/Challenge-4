from random import randint

name = input("What is your name: ")
print("-------------------------------------------")
game_num = randint(1,100)

print(f"Well {name}, I've thought of a number between 1 and 100 and you have only eight tries to guess is. What number do you think it is? ")
print("-------------------------------------------")

tries = 1

for i in range(8):
  tries += 1
  num = int(input("Enter your guess: "))
  if num > 100 or num < 1:
    print("Number is out play.")
    print("-------------------------------------------")
  elif num < game_num:
    print("Number is wrong, the number is also lower than the secret number.")
    print("-------------------------------------------")
  elif num > game_num:
    print("Number is wrong, the number is also greater then the secret number")
    print("-------------------------------------------")
  elif num == game_num:
    print(f"Congratuations you got the right one. It took you {i + 1} times.")
    print("-------------------------------------------")
    break
  elif tries == 8:
    print(f"You were wrong 8 times the secret number was {game_num}.")
    print("-------------------------------------------")
  else:
    print("You are wrong, try again.")
    print("-------------------------------------------")