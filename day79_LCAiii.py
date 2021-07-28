'''
Description
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The nearest common ancestor of two nodes refers to the nearest common node among all the parent nodes of two nodes (including the two nodes).
Return null if LCA does not exist.

node A or node B may not exist in tree.
Each node has a different value

Example
Example1

Input: 
{4, 3, 7, #, #, 5, 6}
3 5
5 6
6 7 
5 8
Output: 
4
7
7
null
Explanation:
  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null
Example2

Input:
{1}
1 1
Output: 
1
Explanation:
The tree is just a node, whose value is 1.
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # create a flag to check if a or b exists respectively
        # helper function return three elements
        a_ex, b_ex, lca = self.helper(root, A, B)
        return lca if (a_ex and b_ex) else None

    def helper(self, node, A, B):
        if not node:
            return False, False, None

        left_a_ex, left_b_ex, left_node = self.helper(node.left, A, B)
        right_a_ex, right_b_ex, right_node = self.helper(node.right, A, B)

        a_ex = left_a_ex or right_b_ex or node == A
        b_ex = left_b_ex or right_b_ex or node == B

        if node == A or node == B:
            return a_ex, b_ex, node

        # other 4 situations
        # if A and B on two sides, return root
        if left_node and right_node:
            return a_ex, b_ex, node
        # if left tree has A or B or LCA
        if left_node:
            return a_ex, b_ex, left_node
        # if right tree has A or B or LCA
        if right_node:
            return a_ex, b_ex, right_node
        # if left tree or right tree doesn't have A or B
        return a_ex, b_ex, None
