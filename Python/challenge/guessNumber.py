from random import choice
import sys
from time import sleep

def guessMyNumber(name: str='PlayerOne'):
  gameCount = 0
  playerWins = 0

  def startGame():
    nonlocal name
    nonlocal gameCount
    nonlocal playerWins       

    print(f"\n{name}, guess which number I'm thinking of... 1, 2 or 3")
    
    playerGuess = input("\nEnter a guess: ")
    computerNums = choice('123')
    
    if playerGuess.isalpha():
      print(f"{name}, please enter 1, 2 or 3.")
      return startGame()
    
    playerGuess = int(playerGuess)
    if playerGuess not in [1, 2, 3]:
        print(f"{name}, please enter 1, 2 or 3.")
        return startGame()
    
    print(f"\n{name}, you chose {playerGuess}")
    sleep(1)
    print(f"I was thinking about the number {computerNums}\n")
    
    gameCount += 1

    def decide_winner(playerGuess, computerNums):
      nonlocal playerWins
      nonlocal name

      if playerGuess == int(computerNums):
        playerWins += 1
        return f"🥳, {name}, you win\n"
      else:
        return f"Sorry, {name}. Better luck next time. 😭\n"

    get_winner = decide_winner(playerGuess, computerNums)
    print(get_winner)

    print(f"Game count: {gameCount}\n")
    print(f"{name}'s wins {playerWins}\n")

    print(f"Your winning percentage is {(playerWins / gameCount) * 1:.2%}")

    print(f"\nPlay again, {name}?")
    print("---------------------------------------------------------")
    print("Y for Yes or\nQ to Quit")

    option = input("Decision: ")[0].lower()

    while option not in ['y', 'q']:
      print(f"Please {name}, enter Yes|(y) or Quit|(q)")
      option = input("Decision: ")[0].lower()

    if option == 'y':
      return startGame()
    elif option == 'q':
      print(f"\n🚀🚀🚀 \tThanks for playing {name}!")
      print(f"Total game(s) played: {gameCount}")
      print(f"Your score is {playerWins} and your percentage is {(playerWins / gameCount) * 1:.2%}")
      print(f'Bye {name} 👋, See you again soon')
      return 1
        
  return startGame

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description = "The is a game where you guess a random number choosen by computer"
    )
    parser.add_argument(
        '-n', '--name', metavar='name', required=True,
        help="The Guessing game"
    )
    args = parser.parse_args()

    game = guessMyNumber(args.name)
    game()
