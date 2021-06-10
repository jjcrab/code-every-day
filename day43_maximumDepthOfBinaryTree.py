

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    # def maxDepth(self, root):
    #     self.maxpath = 0
    #     count = 1
    #     # dfs
    #     self.dfs(root, count)
    #     return self.maxpath

    # def dfs(self, node, count):
    #     if not node:
    #         return
    #     self.maxpath = max(self.maxpath, count)
    #     self.dfs(node.left, count+1)
    #     self.dfs(node.right, count+1)

    def maxDepth(self, root):
        # from leaves to top postorder dfs
        if not root:
            return 0
        left_maxdepth = self.maxDepth(root.left)
        right_maxdepth = self.maxDepth(root.right)

        return max(left_maxdepth, right_maxdepth)+1
