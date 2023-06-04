import guessNumber
import rps8
import sys
from time import sleep

def gameChoice(name='PlayerOne'):
    replay = 0

    def decision():
      nonlocal name
      nonlocal replay

      if replay == 1:
        print('\n---------------------------------------------')
        print(f"\n{name}, welcome back to the Arcade! 🐍")
      else:
        print(f"\n{name}, welcome to the Arcade! 🐍")
      
      print("\nPlease choose a game to play: ")
      print("1 = Rock Paper Scissors")
      print("2 = Guess My Number\n")

      print("Or press \"x\" to exit the Arcade\n")

      choice = input("Decision: ")

      def exitGame():
        print("\nSee you next time!")
        sys.exit(f"Bye {name}!")
      
      if choice.lower() == 'x':
        return exitGame()

      while choice not in ['1', '2'] or choice.isalpha():
        print(f"\n{name}, please enter 1 or 2.")
        choice = input("Decision: ")
        if choice.lower() == 'x':
          return exitGame()
      
      gameChoice = {
          'guessGame': guessNumber.guessMyNumber(name),
          'rps': rps8.rps(name)
      }
      
      choice = int(choice)
      game = ['ROCK PAPER SCISSORS', 'GUESS MY NUMBER']

      print(f"\nYou chose {game[choice - 1]}")
      print(f"\nStarting {game[choice - 1]}...")
      
      sleep(1)

      if choice == 1:
        start = gameChoice['rps']
      else:
        start = gameChoice['guessGame']

      replay = start()

      if replay == 1:
        return decision()
      else:
        exitGame()

    return decision;

if __name__  == '__main__':
  import argparse
  parser = argparse.ArgumentParser(
      description = "The is an arcade game console for you to chaoose a game of your choice"
  )
  parser.add_argument(
      '-n', '--name', metavar='name', required=True,
      help="The Guessing game"
  )
  args = parser.parse_args()
  gameBegins = gameChoice(args.name)
  gameBegins()

