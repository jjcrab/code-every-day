# https: // leetcode.com/problems/insert-delete-getrandom-o1/

'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.mapping = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.mapping:
            self.nums.append(val)
            self.mapping[val] = len(self.nums) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.mapping:
            return False
        # deal with list
        index = self.mapping[val]
        self.nums[index] = self.nums[-1]
        # deal with dict
        self.mapping[self.nums[-1]] = index

        # delete
        self.nums.pop()
        del self.mapping[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return self.nums[random.randint(0, len(self.nums) - 1)]
