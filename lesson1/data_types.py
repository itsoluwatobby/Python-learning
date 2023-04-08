import math
# DATA TYPES

# Strings
## literal assignment
first = "Dave"
last = "Gray"
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
#print(fullname + "!")

#casting a number to a string
# decade = str(1980)
# print(decade)
# print(type(decade))

# statement = "I like rock music from the " + decade + "s."
# print(statement)

#multiple lines
multiline = '''
Hey, how are you?                                           

I was just checking in.
                            All good?

'''
# print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located'
#print(sentence)

# String methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline))
# multiline += "                                                 "
# multiline = "                                             " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

# Build a menu
title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee ".ljust(16, '.') + "$1".rjust(4))
# print("Muffin ".ljust(16, '.') + "$6".rjust(4))
# print("Cheese Cake ".ljust(16, '.') + "$2".rjust(4))
# print("Oriental ".ljust(16, '.') + "$5".rjust(4))

print("")

# # string index value
# print(first[1:])

# # Booleans
# print(first.startswith("D"))
# print(first.endswith('e'))

myValue = True
x = bool(False)
#print(myValue)
#print(x)

# integers
price = 150
best_prie = int(80)
# print(type(price))
# print(isinstance(best_prie,int))

# float
gpa = 3.28
y = float(5.42)
# print(type(gpa))

# complex type
comp_value = 5 + 3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

#Built in func for nums
# print(abs(gpa))

# print(round(gpa))
# print(round(gpa, 1))

# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(gpa))
# print(math.floor(gpa))

# Casting a string to number
zipcode = "10001"
print(int(zipcode))

# Error in casting incorrect data
zip_value = int("New York")
