person='Dave'
coins=3
# print("\n" + person + " has " + str(coins) + " coins left")

# message="\n%s has %s coins left." %(person, coins)
# print(message)

# message="\n{} has {} coins left.".format(person, coins)
# print(message)

# message="\n{1} has {0} coins left.".format(person, coins)
# print(message)

# message="\n{person} has {coins} coins left.".format(person=person, coins=coins)
# print(message)

# player = {'person': 'Dave', 'coins': 3}
# message="\n{person} has {coins} coins left.".format(**player)
# print(message)

#####################################################################
# message = f"\n{person} has {coins} coins left."
# message = f"\n{person} has {78 * 79} coins left."
# message = f"\n{person.title()} has {78 * 79} coins left."
# message = f"\n{player['person']} has {78 * 79} coins left."
# message = f"\n{person[0]} has {78 * 79} coins left."
#print(message)
###############################################
# formatting options
# num = 10
# print(f"\n2.25 times {num} is {2.25 * num:.2f}")

# for num in range(1,11):
#   print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1,11):
  print(f"{num} divided by 4.52 is {num / 4.52:.2%}")

