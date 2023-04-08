# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2= dict(vocals='Plant', guitar='Page')
# print(band)
# print(band.keys())
# print(type(band2))
# print(len(band2))

# print(band.get('guitar'))

# list of key/value pairs as tuples
# print((band.items()))

# verify a key
# print('guitar' in band)
# print('house' in band)

# change values
band['vocals'] = 'Coverdale'  #OR
band.update({'guitar': 'Acoustic'})
band.update({'bass': 'JPJ'})

# print(band2)

# Remove items
# print(band.pop('bass'))
# print(band)

band['drums'] = 'Bonham'
# print(band)

# removing the last item
# print(band.popitem())  #returns a tuple
# print(band)

# Delete and clear
band['drums'] = 'Bonham'
del band['drums']
# print(band)

band2.clear()
# print(band2)
del band2

# copy dictionaries
band2 = band  # only creates a reference / bad copy

band2 = band.copy()
# print("band2: "+str(band2))

# or use the dictionary constructor copy
band3 = dict.copy(band2)  #OR
band4 = dict(band)
# print("Band3: "+str(band3))
# print("Band4: "+str(band4))

# Nested dictionaries
member1 = dict(name='Adrain', surname='Mark', address=dict(street='Bota Qrts', state='Oyo state'), company='samjonesinvestment limited') #OR

member2 = {
    "name" : 'Grace', 
    "surname" : 'Sullivan', 
    "address" : {
        "street" : 'Alimos', 
        "state" : 'Lagos state'
    }, 
    "company" : 'samjonesinvestment limited'
}

band = {
    "member1" : member1,
    "member2" : member2
}

# print(band['member1'])

# SETS

nums = {5, 2, 6, 1, 4, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums2))
print(isinstance(nums2, set))
print(len(nums2))

# True is dupe of 1 and False is dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

print(2 in nums)

# Adding elements to a set
nums.add(9)
print(nums)

more = {8, 7, 6, 12}
nums.update(more)
print(nums)

# merge two sets
one = {1, 2, 3}
two = {4, 5, 6}
three = {9, 2, 8}

newset = one.union(two)
othernewset = one.intersection(three)
# one.intersection_update(three)
brandnewset = three.difference(one)
one.symmetric_difference_update(three)

one.discard(10)
print(one)








