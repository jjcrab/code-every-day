# https: // leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # my way but very slow
        # if head is None or k == 0 or head.next is None:
        #     return head

        # arr = [head]
        # count = 1

        # while arr[-1].next:
        #     arr.append(arr[-1].next)
        # while count <= k % len(arr):
        #     newarr = [arr.pop()]
        #     arr = newarr + arr
        #     count += 1
        # print(arr)
        # dummy = ListNode(0)
        # temp = dummy
        # for i in arr:
        #     temp.next = ListNode(i.val)
        #     temp = temp.next
        # return dummy.next

        # more efficient way
        # edge cases
        if head is None or k == 0 or head.next is None:
            return head
        # write your code here
        dummy = ListNode(0, head)
        # get length
        length = self.getLength(head)
        # ahead and behind
        # k step
        k = k % length
        ahead = behind = dummy.next
        # ahead walk k steps first
        for i in range(k):
            ahead = ahead.next
        # then ahead and behind walk together
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        # break and merge
        ahead.next = dummy.next
        dummy.next = behind.next
        behind.next = None
        return dummy.next
        # getLength function

    def getLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
