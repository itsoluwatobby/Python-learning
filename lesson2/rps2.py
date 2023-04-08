import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playAgain = True

while playAgain:  
  playerChoice = input("\nEnter...\n1 for Rock,\n2 for Paper or \n3 for Scissors:\n\n")

  player = int(playerChoice)

  if player < 1 or player > 3:
      sys.exit("You must enter 1, 2 or 3.")

  computerChoice = random.choice("123")
  computer = int(computerChoice)

  print("\nYou chose "+ str(RPS(player)).replace("RPS.", "") + ".")
  print("\nPython chose "+ str(RPS(computer)).replace("RPS.", "") + ".")

  if player == 1 and computer == 3:
      print("🥳 You win!")
  elif player == 2 and computer == 1:
      print("🥳 You win!")
  elif player == 3 and computer == 2:
      print("🥳 You wins!")
  elif player == computer:
      print("It's a TIE!")
  elif player == 3 and computer == 1:
      print("🐍 Python wins!")
  elif player == 1 and computer == 2:
      print("🐍 Python wins!")
  elif player == 2 and computer == 3:
      print("🐍 Python wins")
  else:
      print("Python wins!")

  print("\nPlay again \nY for Yes\nQ to Quit\n")
  playAgain = input("Response: ")

  if playAgain.lower() == 'y':
      continue
  else:
      print('\n🥳🥳🥳🥳')
      print('Thank you for playing!!')
      playAgain = False

sys.exit('Bye 👋, See you again soon')

