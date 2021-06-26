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

    # method 1:
    # def binaryTreePaths(self, root):
    #     # use dfs
    #     # result
    #     result = []
    #     # path
    #     path = []
    #     # call dfs
    #     self.dfs(root, path, result)
    #     return result

    # def dfs(self, node, path, result):
    #     # end case
    #     if not node:
    #         return
    #     # append node to path
    #     path.append(str(node.val))
    #     # if leaves
    #     if not node.left and not node.right:
    #         path_str = "->".join(path[:])
    #         result.append(path_str)
    #     # traverse
    #     self.dfs(node.left, path, result)
    #     self.dfs(node.right, path, result)
    #     path.pop()

    # method 2:
    # def binaryTreePaths(self, root):
    #         # write your code here
    #     if not root:
    #         return []
    #     return self.dfs(root, str(root.val), [])

    # def dfs(self, node, path, result):
    #     if not node.left and not node.right:
    #         result.append(path)

    #     if node.left:
    #         self.dfs(node.left, path + "->" + str(node.left.val), result)
    #     if node.right:
    #         self.dfs(node.right, path + "->" + str(node.right.val), result)

    #     return result

    # method 3:
    def binaryTreePaths(self, root):
        # write your code here
        result = []
        if not root:
            return result
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if not node.left and not node.right:
            result.append("->".join(path))
            return

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()


# method 4:

    # def binaryTreePaths(self, root):
    #     # use divide and conquer
    #     paths = []
    #     if not root:
    #         return paths

    #     if not root.left and not root.right:
    #         return str(root.val)

    #     left = self.binaryTreePaths(root.left)
    #     for path in left:
    #         paths.append(str(root.val) + "->" + path)

    #     right = self.binaryTreePaths(root.right)
    #     for path in right:
    #         paths.append(str(root.val) + "->" + path)

    #     return paths
