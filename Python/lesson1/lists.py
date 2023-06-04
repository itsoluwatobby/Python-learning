# LISTS
users = ['Dave', 'Sara']
data = ['Mark', 2]
emptyList = []

# print(users[1])
# print(users[0:2])
# print(users[0:])
# print(len(users))

# print(users.index('Sara'))

users.append('Elsa')
#print(users)

users += ['Jason']
#print(users)

users.extend(['Jake', 'Drew'])
#print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
#print(users)

users[2:2] = ['Alex', 'Eddie']
#print(users)

users.remove('Dave')
# print(users)
# print(users.pop())

# del users
# users.clear()
# print(users)

users.sort(key=str.lower)
#print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
#print(nums)

# nums.sort(reverse=True)
# print(nums)

#print(sorted(nums, reverse=True))
#print(nums)

numsCopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]

print("")

# print(nums)
# print(numsCopy)
# print(myNums)
# print(myCopy)

mylist = list([1, 2, True])
# print(mylist)

# TUPLES
myTuples = tuple(('Dave', 42, True))

anotherTuple = (1, 2, 2, 8, 7, 4)

print(myTuples)
print(type(myTuples))
print(type(anotherTuple))

newlist = list(myTuples)
newlist.append('Neil')

newtuple = tuple(newlist)
same = ['hello', 'sam', 'you', 'shade', 4]
print(len(same))

# (one, *two, hey) = same
# print(one)
# print(two)
# print(hey)

print(anotherTuple.count(5))

