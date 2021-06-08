# https://leetcode.com/problems/leaf-similar-trees/
'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:

Input: root1 = [1], root2 = [1]
Output: true
Example 3:

Input: root1 = [1], root2 = [2]
Output: false
Example 4:

Input: root1 = [1,2], root2 = [2,2]
Output: true
Example 5:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
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
    @param root1: the first tree
    @param root2: the second tree
    @return: returns whether the leaf sequence is the same
    """
    # def leafSimilar(self, root1, root2):
    #     # root1 list, root2 list
    #     if not root1 and root2:
    #         return False
    #     if not root2 and root1:
    #         return False
    #     if not root1 and not root2:
    #         return True
    #     root1_list=[]
    #     root2_list=[]
    #     self.helper(root1,root1_list)
    #     self.helper(root2,root2_list)
    #     return root1_list == root2_list

    # def helper(self,node,list):
    #     #dfs
    #     #end case
    #     if node is None:
    #         return -1
    #     left_level=self.helper(node.left,list)
    #     right_level=self.helper(node.right,list)
    #     cur_level = max(left_level,right_level)+1
    #     if cur_level == 0:
    #         list.append(node.val)
    #     return cur_level

    def leafSimilar(self, root1, root2):
        leaves1, leaves2 = [], []
        self.dfs(root1, leaves1)
        self.dfs(root2, leaves2)
        return leaves1 == leaves2

    def dfs(self, node, leaves):
        if not node:
            return
        # preorder traverse
        if not node.left and not node.right:
            leaves.append(node.val)
        self.dfs(node.left, leaves)
        self.dfs(node.right, leaves)
