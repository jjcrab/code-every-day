'''
Description
The size of the hash table is not determinate at the very beginning. If the total size of keys is too large (e.g. size >= capacity / 10), we should double the size of the hash table and rehash every keys. Say you have a hash table looks like below:

size=3, capacity=4

[null, 21, 14, null]
       ↓    ↓
       9   null
       ↓
      null
The hash function is:

int hashcode(int key, int capacity) {
    return key % capacity;
}
here we have three numbers, 9, 14 and 21, where 21 and 9 share the same position as they all have the same hashcode 1 (21 % 4 = 9 % 4 = 1). We store them in the hash table by linked list.

rehashing this hash table, double the capacity, you will get:

size=3, capacity=8

index:   0    1    2    3     4    5    6   7
hash : [null, 9, null, null, null, 21, 14, null]
Given the original hash table, return the new hash table after rehashing .

For negative integer in hash table, the position can be calculated as follow:

C++/Java: if you directly calculate -4 % 3 you will get -1. You can use function: a % b = (a % b + b) % b to make it is a non negative integer.
Python: you can directly use -1 % 3, you will get 2 automatically.
0 <= capacity <= 20000<=capacity<=2000
0 <= size <= 100000<=size<=10000

Example
Example 1:

Input:

hashTable = [null, 21->9->null, 14->null, null]
Output:

[null, 9->null, null, null, null, 21->null, 14->null, null]
Explanation:

Double the capacity of the hash table and rearrange all the hash values.
'''


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """

    def rehashing(self, hashTable):
        ori_size = len(hashTable)
        new_size = 2 * ori_size
        new_hashTable = [None for i in range(new_size)]

        # loop into the original hash new_hashTable
        for i in hashTable:
            # if not i:
            #     continue

            while i:
                # get new hashcode
                new_position = i.val % new_size
                # if the new hashcode in new hashtable is empty
                if not new_hashTable[new_position]:
                    new_hashTable[new_position] = ListNode(i.val)
                # if the new hashcode in new hashtable is not empty
                else:
                    # add the key to the end of the linked list
                    self.addlistnode(new_hashTable[new_position], i.val)
                # check next node in original hashtable
                i = i.next

        return new_hashTable

    def addlistnode(self, node, val):
        while node.next:
            node = node.next
        node.next = ListNode(val)
