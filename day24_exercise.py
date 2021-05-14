# x = None
# if not x:
#     print('if x')
# if x is not None:
#     print('if x is not None')

# x = []
# if x:
#     print('if x')
# if x is not None:
#     print('if x is not None')


# list1 = [1, 4, 2]
# # list2 = list1
# list2 = [i for i in list1]
# list2.append('o')
# print(list1)


def indexOf(self, list, val):
    if val in list:
        return list.index(val)
    else:
        return -1
