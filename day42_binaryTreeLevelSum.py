'''
Given a binary tree and an integer which is the depth of the target level.

Calculate the sum of the nodes in the target level.

Example
Example 1:

Input：{1,2,3,4,5,6,7,#,#,8,#,#,#,#,9},2
Output：5 
Explanation：
     1
   /   \
  2     3
 / \   / \
4   5 6   7
   /       \
  8         9
2+3=5
Example 2:

Input：{1,2,3,4,5,6,7,#,#,8,#,#,#,#,9},3
Output：22
Explanation：
     1
   /   \
  2     3
 / \   / \
4   5 6   7
   /       \
  8         9
4+5+6+7=22
'''


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """

    # def levelSum(self, root, level):
    #     # use BFS
    #     # set queue
    #     queue = collections.deque([root])
    #     # set a result list of each level
    #     result = []
    #     # edge case
    #     if not root or level < 1:
    #         return 0
    #     if level == 1:
    #         return root.val

    #     # add nodes in to each level
    #     while queue:
    #         layer = []
    #         n = len(queue)
    #         for i in range(n):
    #             node = queue.popleft()
    #             layer.append(node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         result.append(layer)
    #     # take the element in result list which is the target level
    #     # sum the nodes in that element
    #     # edge case
    #     if len(result) < level:
    #         return 0
    #     return sum(result[level-1])

    def levelSum(self, root, level):
        # use dfs
        # set layer
        layer = []
        # set count
        count = 1
        # call dfs
        self.dfs(root, layer, count, level)
        # return
        return sum(layer)

    def dfs(self, node, layer, count, level):
        # end case
        if not node:
            return
        # target layer
        if count == level:
            # add the node to the layer list
            layer.append(node.val)
            return

        # recursive/traverse
        self.dfs(node.left, layer, count+1, level)
        self.dfs(node.right, layer, count+1, level)
