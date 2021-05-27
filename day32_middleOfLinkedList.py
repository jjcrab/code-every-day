# https: // leetcode.com/problems/middle-of-the-linked-list/solution/

# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # dummy = ListNode(0,head)
        # cur = dummy.next
        # length = 1
        # while cur.next is not None:
        #     cur = cur.next
        #     length += 1
        # if length % 2 == 0:
        #     mid = length/2 - 1
        # else:
        #     mid = length//2
        # cur = dummy.next
        # count = 0
        # while count< mid:
        #     cur = cur.next
        #     count += 1
        # return cur

        # slow = head
        # fast = head
        # while fast and fast.next is not None:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow

        arr = [head]
        while arr[-1].next is not None:
            arr.append(arr[-1].next)

        return arr[len(arr)//2]

# print(4/2)
# print(4//2)
# print(int(4/2))
