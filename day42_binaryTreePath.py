# https://leetcode.com/problems/binary-tree-paths/
'''
Description
Given a binary tree, return all root-to-leaf paths.

Example
Example 1:

Input：{1,2,3,#,5}
Output：["1->2->5","1->3"]
Explanation：
   1
 /   \
2     3
 \
  5
Example 2:

Input：{1,2}
Output：["1->2"]
Explanation：
   1
 /   
2     

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
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # use dfs
        # result
        result = []
        # path
        path = []
        # call dfs
        self.dfs(root, path, result)
        return result

    def dfs(self, node, path, result):
        # end case
        if not node:
            return
        # append node to path
        path.append(str(node.val))
        # if leaves
        if not node.left and not node.right:
            path_str = "->".join(path[:])
            result.append(path_str)
        # traverse
        self.dfs(node.left, path, result)
        self.dfs(node.right, path, result)
        path.pop()
