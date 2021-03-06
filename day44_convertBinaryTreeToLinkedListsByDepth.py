'''
Description
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

Example
Example 1:

Input: {1,2,3,4}
Output: [1->null,2->3->null,4->null]
Explanation: 
        1
       / \
      2   3
     /
    4
Example 2:

Input: {1,#,2,3}
Output: [1->null,2->null,3->null]
Explanation: 
    1
     \
      2
     /
    3
'''

import collections
# Definition of TreeNode:


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):

        # use bfs
        res = []
        if not root:
            return res
        queue = collections.deque([root])

        # while outer loop
        while queue:
            dummy = ListNode(-1)
            layer = dummy
            n = len(queue)
        # for inner loop
            for i in range(n):
                node = queue.popleft()
                layer.next = ListNode(node.val)
                layer = layer.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(dummy.next)

        return res
