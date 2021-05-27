# https: // leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
Description
Given a linked list, remove the nth node from the end of list and return its head.

The minimum number of nodes in list is n.

Example
Example 1:
	Input: list = 1->2->3->4->5->null， n = 2
	Output: 1->2->3->5->null


Example 2:
	Input:  list = 5->4->3->2->1->null, n = 2
	Output: 5->4->3->1->null
Challenge
Can you do it without getting the length of the linked list?
'''


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # my way
        #     # get length
        #     length = self.getLength(head)
        #     # edge case:
        #     if length == 1 and n == 1 or head is None:
        #         return None
        #     if length == n:
        #         return head.next

        #     # break and merge
        #     count = 0
        #     dummy = ListNode(0, head)
        #     while count < length - n - 1:
        #         head = head.next
        #         count += 1

        #     head.next = head.next.next
        #     return dummy.next
        #     # getLength method

        # def getLength(self, head):
        #     length = 0
        #     while head:
        #         head = head.next
        #         length += 1
        #     return length

        # two pointers way
        # edge cases:
        dummy = ListNode(0, head)
        #fast and slow
        # fast goes n step ahead
        fast = slow = dummy
        for i in range(n):
            fast = fast.next
            # fast and slow go together
        while fast.next:
            fast = fast.next
            slow = slow.next
        # break and merge
        slow.next = slow.next.next

        return dummy.next
