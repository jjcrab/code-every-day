# https://leetcode.com/problems/validate-binary-search-tree/

'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Example
Example 1:

Input:

tree = {-1}
Output:

true
Explanation:

For the following binary tree（only one node）:
              -1
This is a binary search tree.
Example 2:

Input:

tree = {2,1,4,#,#,3,5}
Output:

true
Explanation:

For the following binary tree:
          2
         / \
        1   4
           / \
          3   5
This is a binary search tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # use inorder dfs
        res = []
        # call dfs
        self.dfs(root, res)
        # condition
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        return True

    def dfs(self, node, res):
        if not node:
            return
        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)
