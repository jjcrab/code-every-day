'''
Description
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
Example 1:

add(1); add(3); add(5);
find(4) // return true
find(7) // return false
'''


class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        # list
        # self.array = []
        # use dict
        self.dic = {}

    def add(self, number):
        # list
        # self.array.append(number)

        # list O(N) insert sort
        # self.array.append(number)
        # index = len(self.array) - 1
        # while index > 1 and self.array[index] < self.array[index - 1]:
        #     self.array[index], self.array[index - 1] = self.array[index - 1], \
        #         self.array[index]
        #     index -= 1

        # dic
        # if number in self.dic:
        #     self.dic[number] += 1
        # else:
        #     self.dic[number] = 1
        self.dic[number] = self.dic.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # list
        # two pointers
        # self.array.sort()
        # left, right = 0, len(self.array) - 1
        # while left < right:
        #     if self.array[left] + self.array[right] == value:
        #         return True
        #     elif self.array[left] + self.array[right] > value:
        #         right -= 1
        #     else:
        #         left += 1
        # return False

        # dic
        for key in self.dic:
            # duplicate
            if value - key == key:
                if self.dic[key] > 1:
                    return True
                else:
                    return False
            elif value - key in self.dic:
                return True

            # if value - key in self.dic and \
            #     (value - key != key or self.dic[key] > 1):
            #     return True

        return False
