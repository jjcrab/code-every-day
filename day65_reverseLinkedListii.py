'''
Description
Reverse a linked list from position m to n.

m and n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list1≤m≤n≤lengthoflist.

Example
Example 1:

Input:

linked list = 1->2->3->4->5->NULL
m = 2
n = 4
Output:

1->4->3->2->5->NULL
Explanation:

Reverse the [2,4] position of the linked list.

Example 2:

Input:

linked list = 1->2->3->4->null
m = 2
n = 3
Output:

1->3->2->4->NULL
Explanation:

Reverse the [2,3] position of the linked list.

Challenge
Reverse it in-place and in one-pass


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
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1, head)
        # find the position and break connection
        pre_mth = self.find_index(dummy, m - 1)
        # record mth because after connect to another node it can't be found
        mth = pre_mth.next
        nth = self.find_index(dummy, n)
        # record nth.next because after break the connection it can't be found
        nth_next = nth.next
        nth.next = None
        # pre_mth.next = None

        self.reverse(mth)

        # reconnect
        pre_mth.next = nth
        mth.next = nth_next
        return dummy.next

    def reverse(self, head):
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre

    def find_index(self, head, k):
        for _ in range(k):
            if not head:
                return head
            head = head.next
        return head
