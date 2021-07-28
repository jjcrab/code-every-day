'''
Description
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

Assume two nodes are exist in tree.

Example
Example 1:

Input:

tree = {1}
A = 1
B = 1
Output:

1
Explanation:

For the following binary tree（only one node）:
        1
LCA(1,1) = 1
Example 2:

Input:

tree = {4,3,7,#,#,5,6}
A = 3
B = 5
Output:

4
Explanation:

For the following binary tree:

     4
    / \
   3   7
      / \
     5   6

LCA(3, 5) = 4

'''


def lowestCommonAncestor(self, root, A, B):
    if not root:
        return None
    if root == A or root == B:
        return root

    # if A and B, return LCA
    # if only A, return A
    # if only B, return B
    # if not A and not B, return None

    left = self.lowestCommonAncestor(root.left, A, B)
    right = self.lowestCommonAncestor(root.right, A, B)

    # if A and B on two sides, return root
    if left and right:
        return root
    # if left tree has A or B or LCA
    if left:
        return left
    # if right tree has A or B or LCA
    if right:
        return right
    # if left tree or right tree doesn't have A or B
    return None
