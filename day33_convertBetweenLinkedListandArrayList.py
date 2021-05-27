# Convert Linked List to Array List
# Convert a linked list to an array list.
# Example
# Example 1:

# Input: 1 -> 2 -> 3 -> null
# Output: [1, 2, 3]
# Example 2:

# Input: 3 -> 5 -> 8 -> null
# Output: [3, 5, 8]
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the head of linked list.
    @return: An integer list
    """

    def toArrayList(self, head):
        # if not head:
        #     return []
        # arr = [head.val]
        # while head.next:
        #     head = head.next
        #     arr.append(head.val)
        # return arr
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr


'''
Convert Array List to Linked List
Description
Convert an array list to a linked list.

Example
Example 1:

Input: [1,2,3,4], 
Output: 1->2->3->4->null.
Example 2:

Input: [1,2], 
Output: 1->2->null.
'''

# Definition of ListNode


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: nums: an integer array
    @return: the first node of linked list
    """

    def toLinkedList(self, nums):
        # if not nums:
        #     return None

        # dummy = ListNode(0)
        # head = ListNode(nums[0])
        # dummy.next = head

        # for i in range(1, len(nums)):
        #     head.next = ListNode(nums[i])
        #     head = head.next
        # return dummy.next

        # head, temp = None, None
        # for i in nums:
        #     if head is None:
        #         head = ListNode(i)
        #         temp = head
        #     else:
        #         temp.next = ListNode(i)
        #         temp = temp.next
        # return head

        dummy = ListNode(0)
        head = dummy
        for i in nums:
            head.next = ListNode(i)
            head = head.next
        return dummy.next
