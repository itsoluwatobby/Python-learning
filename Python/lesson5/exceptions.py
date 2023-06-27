class JustNotCoolError(Exception):
    pass


x = {'name': 'mark'}
y = 2
try:
    # raise Exception("I'm a custom exception")

    # CUSTOM EXCEPTION
    raise JustNotCoolError('This is not cool at all')

    # print(x.get('name'))
    # if not type(x) is str:
    #     raise TypeError('Only strings are allowed')
except NameError:
    print('NameError means something is undefined')
except ZeroDivisionError:
    print('ZeroDivisionError: Dont\'t divide by zero')
except AttributeError:
    print('AttributeError: attribute name not found in x')
except Exception as error:
    print(error)
else:
    print('No errors')
finally:
    print('I\'m always going to print')
 
