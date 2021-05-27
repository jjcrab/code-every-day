
'''
Insert Node in Sorted Linked List


Description
Insert a node in a sorted linked list.

Example
Example 1:

Input: head = 1->4->6->8->null, val = 5
Output: 1->4->5->6->8->null
Example 2:

Input: head = 1->null, val = 2
Output: 1->2->null
'''


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """

    def insertNode(self, head, val):

        # dummy = ListNode(0)
        # dummy.next = head

        # insert_node = ListNode(val)

        # pre = dummy
        # cur = head
        # if head is None:
        #     return insert_node

        # while cur:
        #     if cur.val <= val:
        #         pre = cur
        #         cur = cur.next
        #     else:
        #         pre.next = insert_node
        #         insert_node.next = cur
        #         return dummy.next

        # pre.next = insert_node
        # return dummy.next

        dummy = ListNode(0, head)
        pre = dummy
        while pre.next and pre.next.val < val:
            pre = pre.next
        newNode = ListNode(val, pre.next)
        pre.next = newNode
        return dummy.next
