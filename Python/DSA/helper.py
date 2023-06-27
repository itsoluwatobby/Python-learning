
def arrLength(array: list[int | str]):
    cusLength = 0
    while True:
        try:
            array[cusLength]
            cusLength += 1
        except IndexError:
            break
    return cusLength


first = [1, 3, 2, 5, 7, 8, 9]
second = [5, 4, 8]

empty: list[int] = []
# for x in range(len(second)):
#     ind = 3 + x
# first = empty + first[-1]
print(first)
