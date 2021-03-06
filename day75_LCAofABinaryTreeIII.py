'''
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    # one way
    # def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

    # p1, p2 = p, q
    # while p1 != p2:
    #     p1 = p1.parent if p1.parent else q
    #     p2 = p2.parent if p2.parent else p

    # return p1

    # easier to understand way
    def lowestCommonAncestorII(self, root, A, B):
        # use set()
        ancestors = set([A])
        node = A
        while A.parent:
            ancestors.add(A.parent)
            A = A.parent

        node_b = B
        while node_b not in ancestors:
            node_b = node_b.parent

        return node_b
