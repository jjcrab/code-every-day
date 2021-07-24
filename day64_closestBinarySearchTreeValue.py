'''
Description
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example
Example1

Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
Example2

Input: root = {3,2,4,1} and target = 4.142857
Output: 4
Explanation：
Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1

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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    # def closestValue(self, root, target):
    #     result = []
    #     self.dfs(root, result)
    #     print(result)
    #     for i in range(len(result)):
    #         if result[i] > target:
    #             if abs(result[i - 1] - target) > abs(result[i] - target):
    #                 return result[i]
    #             else:
    #                 return result[i - 1]

    #     return result[-1]

    # def dfs(self, node, result):
    #     if not node:
    #         return
    #     if node.left:
    #         self.dfs(node.left, result)
    #     result.append(node.val)
    #     if node.right:
    #         self.dfs(node.right, result)

# better way to do it, Time: O(H), space: O(1)
    def closestValue(self, root, target):
        lower, upper = root, root
        while root:
            # result on the right, set lower bound
            if target > root.val:
                lower = root
                root = root.right
            # result on the left, set upper bound
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root.val

        if abs(target - lower.val) >= abs(target - upper.val):
            return upper.val
        else:
            return lower.val
