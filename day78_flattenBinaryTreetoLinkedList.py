'''
Description
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

Example
Example 1:

Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
Example 2:

Input:{1}
Output:{1}
Explanation：
         1
         1
Challenge
Do it in-place without any extra memory.
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
# O(N) & O(1)

    def flatten(self, root):
        if not root:
            return None
        node = root
        while node:
            # if node has left child
            if node.left:
                # find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                # rewrite the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None

            # move on the right side of the tree
            node = node.right

# O(N) and O(N)
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right


# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         # Do not return anything, modify root in-place instead.
#         self.flattenTree(root)

#     def flattenTree(self, node):
#         if not node:
#             return None
#         # leaf node
#         if not node.left and not node.right:
#             return node
#         leftTail = self.flattenTree(node.left)
#         rightTail = self.flattenTree(node.right)

#         # connect, if there was a left subtree, shuffle around
#         if leftTail:
#             leftTail.right = node.right
#             node.right = node.left
#             node.left = None

#         return rightTail if rightTail else leftTail
