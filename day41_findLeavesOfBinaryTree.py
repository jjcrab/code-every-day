# https://leetcode.com/problems/find-leaves-of-binary-tree/
'''
Description
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example
Example1
Input: {1,2,3,4,5}
Output: [[4, 5, 3], [2], [1]].
 1
   / \
  2   3
 / \     
4   5  

Example2
Input: {1,2,3,4}
Output: [[4, 3], [2], [1]].
Explanation:

    1
   / \
  2   3
 /
4 
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
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """

    def findLeaves(self, root):
        # set a result list
        result = []
        # edge case
        if root is None:
            return result
        # dfs
        self.dfs(root, result)
        # return
        return result

    def dfs(self, node, result):
        # end case
        if node is None:
            return -1
        # postorder traverse
        left_level = self.dfs(node.left, result)
        right_level = self.dfs(node.right, result)
        # current level
        cur_level = max(left_level, right_level)+1
        # add node to current level
        self.addleaves(cur_level, result, node.val)
        # return current level
        return cur_level

    def addleaves(self, level, result, value):
        if len(result) == level:
            result.append([])
        result[level].append(value)
