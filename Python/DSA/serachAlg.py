from helper import arrLength

class Array:
   # i: int = 0
    def __init__(self, length=10, arr: list[str | int] = []):
        self.length = length
        self.arr = arr

    def getDefaultLength(self):
        self.length = arrLength(self.arr)
        return f'Default length is: {self.length}'

    def getLength(self):
        self.length = arrLength(self.arr)
        return f'length is: {self.length}'

    def addItem(self, args: list[str | int] = []):
        if arrLength(args) > self.length:
            self.length *= 2
        self.arr = self.arr + args

    def removeItem(self, targ: str | int):
        i = 0
        self.arr = [ind for ind in self.arr if ind != targ]
        self.printElements()
    
    def printReverse(self):
        new_arr = []
        size = self.length
        while True:
            try:
                self.arr = new_arr + self.arr[size - 1]
                size -= 1
            except IndexError:
                break
        self.printElements()

    def printElements(self):
        return self.arr


my_array = Array(10, ['sam', 'mark', 'john', 'dam'])
print(my_array.getLength())
my_array.addItem(['olu', 'mark', 'adam', 5, 6, 4, 8, 7])
print(my_array.printElements())
print(my_array.getLength())
my_array.addItem([12, 5, 6, 'kan', 'malu', 'adam', 50, 'fido', 41, 'saro'])
print(my_array.printElements())
print(my_array.getDefaultLength())
print(my_array.removeItem('malu'))
print(my_array.printElements())
print(my_array.printReverse())
