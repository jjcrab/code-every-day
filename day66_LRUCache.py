'''
Description
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Finally, you need to return the data from each get.

Example
Example1

Input:
LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)
Output: [1,-1,1]
Explanation：
cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) and return 1.
Example 2:

Input：
LRUCache(1)
set(2, 1)
get(2)
set(3, 2)
get(2)
get(3)
Output：[1,-1,2]
Explanation：
cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.

'''


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return self.cache[key]
        return -1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key not in self.cache and len(self.cache) == self.capacity:
            # last = True if follow FILO, last = False if follow FIFO
            self.cache.popitem(last=False)
        elif key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value
