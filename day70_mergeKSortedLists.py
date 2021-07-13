# https://leetcode.com/problems/merge-k-sorted-lists/
'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:


Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
# # lists = []
# if not lists:
#     return None

# node_list = []
# for i in lists:
#     # lists = [[], [1]]
#     if not i:
#         continue
#     head = i
#     dummy = ListNode(-1, i)
#     while head:
#         node_list.append(head.val)
#         head = head.next
# # lists = [[], []]
# if not node_list:
#     return None

# node_list.sort()
# head = ListNode(node_list[0])
# dummy = ListNode(-1, head)
# for i in range(1, len(node_list)):
#     head.next = ListNode(node_list[i])
#     head = head.next

# return dummy.next


# use merge sort with divide and conquer

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # use merge sort with divide and conquer

        # edge case:
        if not lists:
            return None
        return self.divide_merge(lists, 0, len(lists) - 1)

    def divide_merge(self, lists, start, end):
        # end case:
        if start >= end:
            return lists[start]

        mid = (start + end) // 2
        left = self.divide_merge(lists, start, mid)
        right = self.divide_merge(lists, mid + 1, end)
        return self.merge(left, right)

    def merge(self, head1, head2):
        tail = dummy = ListNode(-1)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                tail = tail.next
                head1 = head1.next
            else:
                tail.next = head2
                tail = tail.next
                head2 = head2.next

        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        return dummy.next
