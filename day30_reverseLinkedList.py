
# https: // leetcode.com/problems/reverse-linked-list/submissions/
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        cur = None
        while head is not None:
            temp = head.next
            head.next = cur
            cur = head
            head = temp
        return cur
