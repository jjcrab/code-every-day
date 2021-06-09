'''
Description
Given a binary tree, calculate the sum of leaves.

Example
Example 1:

Input：{1,2,3,4}
Output：7
Explanation：
    1
   / \
  2   3
 /
4
3+4=7
Example 2:

Input：{1,#,3}
Output：3
Explanation：
    1
      \
       3

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
    @param root: the root of the binary tree
    @return: An integer
    """

    def leafSum(self, root):
        # use dfs
        # leaves list
        leaves = []
        # call dfs
        self.dfs(root, leaves)
        # return sum
        return sum(leaves)

    def dfs(self, node, leaves):
        # end case
        if not node:
            return
        # if leaves
        if not node.left and not node.right:
            leaves.append(node.val)

        # traverse
        self.dfs(node.left, leaves)
        self.dfs(node.right, leaves)
