# https: // leetcode.com/problems/binary-tree-inorder-traversal/

'''
Given a binary tree, return the inorder traversal of its nodes‘ values.

Example
Example 1:

Input:

binary tree = {1,2,3}
Output:

[2,1,3]
Explanation:

   1
/  \
2     3
It will be serialized as {1,2,3} inorder traversal

Example 2:

Input:

binary tree = {1,#,2,3}
Output:

[1,3,2]
Explanation:

1
\
2
/
3
It will be serialized as {1,#,2,3} inorder traversal
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
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        #     # inorder dfs
        #     res = []
        #     # call dfs
        #     self.dfs(root, res)
        #     return res

        # def dfs(self, node, res):
        #     if not node:
        #         return
        #     if node.left:
        #         self.dfs(node.left, res)
        #     res.append(node.val)
        #     if node.right:
        #         self.dfs(node.right, res)

        # iteration solution
        stack = []
        result = []
        # add all the left to stack
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            result.append(node.val)
        # add right to the stack
            root = node.right

        return result
