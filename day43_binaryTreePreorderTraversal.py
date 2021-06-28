# https: // leetcode.com/problems/binary-tree-preorder-traversal/

'''
Description
Given a binary tree, return the preorder traversal of its nodes' values.

The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
Example
Example 1:

Input:

binary tree = {1,2,3}
Output:

[1,2,3]
Explanation:

   1
/  \
2     3
It will be serialized as {1,2,3} preorder traversal

Example 2:

Input:

binary tree = {1,#,2,3}
Output:

[1,2,3]
Explanation:

1
\
2
/
3
It will be serialized as {1,#,2,3} preorder traversal

Challenge
Can you do it without recursion?
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
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # use dfs
        result = []
        # call dfs
        self.dfs(root, result)
        return result

    def dfs(self, node, result):
        if not node:
            return
        result.append(node.val)
        self.dfs(node.left, result)
        self.dfs(node.right, result)


# iteration solution:
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         stack, res = [root], []
#         if not root:
#             return res
#         while stack:
#             node = stack.pop()
#             if node:
#                 res.append(node.val)
#                 if node.right:
#                     stack.append(node.right)
#                 if node.left:
#                     stack.append(node.left)

#         return res
