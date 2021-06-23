# Binary Tree Level Order Traversal

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
Example
Example 1:

Input:

tree = {1,2,3}
Output:

[[1],[2,3]]
Explanation:

   1 
  / \ 
 2   3 
it will be serialized {1,2,3}
Example 2:

Input:

tree = {1,#,2,3} 
Output:

[[1],[2],[3]] 
Explanation:

1 
 \ 
  2 
 / 
3 
it will be serialized {1,#,2,3}

Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use BFS algorithm to do it.
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""




import collections
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # use one Queue
        result = []
        if not root:
            return result

        # create a Queue
        queue = collections.deque([root])
        # loop each level and each node
        while queue:
            result.append([i.val for i in queue])
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

        # use two lists
        # result = []
        # while not root:
        #     return result

        # current_level = [root]
        # while current_level:
        #     next_level = []
        #     result.append([node.val for node in current_level])
        #     for node in current_level:
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     current_level = next_level

        # return result

        # use dummy node and queue and list
        # dummyNode
        # result = []
        # level = []
        # if not root:
        #     return result
        # queue = collections.deque([root, None])
        # while queue:
        #     node = queue.popleft()
        #     if node is None:
        #         result.append(level)
        #         level = []
        #         if queue:
        #             queue.append(None)
        #         continue
        #     level.append(node.val)
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)

        # return result
