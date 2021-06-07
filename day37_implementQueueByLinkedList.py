
# Implement a Queue by linked list. Support the following basic methods:

# enqueue(item). Put a new item in the queue.
# dequeue(). Move the first item out of the queue, return it.
# Example
# Example 1:

# Input:
# enqueue(1)
# enqueue(2)
# enqueue(3)
# dequeue() // return 1
# enqueue(4)
# dequeue() // return 2
# Example 2:

# Input:
# enqueue(10)
# dequeue() // return 10


class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """

    def __init__(self):
        self.head = self.dummy = LinkedNode(0)

    def enqueue(self, item):
        # write your code here
        self.head.next = LinkedNode(item)
        self.head = self.head.next

    """
    @return: An integer
    """

    def dequeue(self):
        # write your code here
        if not self.dummy.next:
            return -1
        else:
            value = self.dummy.next.val
            # self.dummy.next = self.dummy.next.next (can't delete one node since head might got deleted if only one node there)
            self.dummy = self.dummy.next
        return value
