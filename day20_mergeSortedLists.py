# https: // leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    # l1.extend(l2)
    # return sorted(l1)
    head = ListNode()
    cur = head
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return head.next


def createlist(inp):
    l1 = ListNode()
    cur = l1
    for t in inp:
        cur.next = ListNode(t)
        cur = cur.next
    cur = l1.next
    return cur


def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")


list1 = createlist([2, 4, 6])
list2 = createlist([1, 3, 5])
ans = mergeTwoLists(list1, list2)
prettyPrintLinkedList(ans)
