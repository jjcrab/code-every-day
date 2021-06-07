# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [20, 9], [15, 7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        # use two stacks
        stack = [root]
        next_stack = []
        # flag
        left_to_right = True
        # result
        result = []
        # outer loop for layer
        while stack:
            # current level nodes
            cur_level = []
            # inner loop for each node
            while stack:
                cur_node = stack.pop()
                if cur_node:
                    cur_level.append(cur_node.val)
                    # if flag, append left and right to next stack
                    if left_to_right:
                        next_stack.append(cur_node.left)
                        next_stack.append(cur_node.right)
                    # if not flag, append right and left to next stack
                    else:
                        next_stack.append(cur_node.right)
                        next_stack.append(cur_node.left)
                elif not cur_node:
                    continue
            # switch stack and next stack
            stack, next_stack = next_stack, stack
            # add current level nodes to result
            if cur_level:
                result.append(cur_level)
            # change flag
            left_to_right = not left_to_right

        return result


# use deque method
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        # set deque
        queue = collections.deque([root])
        # set flag
        left_to_right = True
        # set result
        result = []
        # outer loop for layer
        while queue:
            # current layer
            cur_layer = []
            # inner loop for each node
            n = len(queue)
            for i in range(n):
                # current node
                cur_node = queue.popleft()
                # add value to current layer
                cur_layer.append(cur_node.val)
                # setup next layer
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

            # if not flag, reverse current layer
            if not left_to_right:
                cur_layer.reverse()
            # add current layer to result
            result.append(cur_layer)
            # switch flag
            left_to_right = not left_to_right
        return result
