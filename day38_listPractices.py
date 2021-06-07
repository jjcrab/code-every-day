import math
import random

num = random.randrange(1, 10)
print(num)

evenList = [i*2 for i in range(4)]
print(evenList)


numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_values = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                  for m in numList]
print(list_of_values)


# multi dimention list
listTable = [[0]*4 for i in range(4)]
for i in range(4):
    for j in range(4):
        listTable[i][j] = i, j
print(listTable)


table = [[0]*9 for i in range(9)]
for i in range(9):
    for j in range(9):
        table[i][j] = (i+1)*(j+1)
        print(table[i][j], end=",")
    print()
# for item in table:
#     print(item)
