
def hello():
    print('hello world')

hello()

def sum(num1:int = 0, num2:int = 0)  -> int :
    if type(num1) is not int or type(num2) is not int:
        return 0
    return (num1 + num2)

total = sum(1, 1)
# print(total)

def multiple_items(*args):
    print(args) 
    print(type(args))

multiple_items('Dave', 'John', 'Sam')

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first ='Dave', second='John', last='Sam')


