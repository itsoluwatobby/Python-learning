
from functools import reduce
from enum import Enum


def squared(num): return num * num


# squared = lambda num: num * num
#print(squared(5))


def addTwo(num): return num + 2


# addTwo = lambda num: num + 2
#print(addTwo(12))


def sum_total(a, b): return a + b


# sum_total = lambda a, b: a + b
#print(sum_total(2, 6))

###############################################


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)
#print(addTen(7))
#print(addTwenty(7))

#########################################
# HIGHER OTHER FUNCTIONS

numbers = [3, 7, 12, 18, 20, 21]
squared_nums = map(lambda num: num * num, numbers)
#print(list(squared_nums))

##############################
odd_nums = filter(lambda num: num % 2 != 0, numbers)
#print(list(odd_nums))

add_nums = reduce(lambda accumulator,
                  current: accumulator + current, numbers, 0)
#print(add_nums)
#print(sum(numbers, 0))

add_len = lambda acc, curr: acc + len(curr)
names = ['sarah', 'dave gray', 'itsoluwatobby']
char_count=reduce(add_len, names, 0)
print(char_count)
