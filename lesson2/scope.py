name = 'Dave'
count = 1

def another():
  color = 'Blue'
  global count
  count += 1
  print(count)
  print(color)

  def greeting(name):
    nonlocal color
    color = 'red'
    print(color)
    print(name)
    return 547.4//10

  result = greeting('Dave')
  print(result)

another()

# ************** CLOSURES **************************
# Closure is a function having access to the scope of it's parent function after the parent's function has returned / is closed

def parent_function(person, coins = 3):
  # coins = 3

  def play_game():
    nonlocal coins
    coins -= 1

    if coins > 1:
      print('\n' + person + ' has ' + str(coins) + ' coins left')
    elif coins == 1:
      print('\n' + person + ' has ' + str(coins) + ' coin left')
    else:
      print('\n' + person + ' is out of coins')
  
  return play_game

tommy = parent_function('Tommy')
jenny = parent_function('Jenny', 5)

tommy()
tommy()
jenny()


