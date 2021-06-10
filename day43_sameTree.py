# https://leetcode.com/problems/same-tree/solution/

'''

Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.

Example
Example 1:

Input:{1,2,2,4},{1,2,2,4}
Output:true
Explanation:
        1                   1
       / \                 / \
      2   2   and         2   2
     /                   /
    4                   4

are identical.
Example 2:

Input:{1,2,3,4},{1,2,3,#,4}
Output:false
Explanation:

        1                  1
       / \                / \
      2   3   and        2   3
     /                        \
    4                          4

are not identical.
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
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """

    def isIdentical(self, a, b):
        # end case
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        # print(3)

        # traverse (Flase and ... always False, so when the first condition is \
        # false will stop so doesn't go through the right child tree "2")
        return self.isIdentical(a.left, b.left) \
            and self.isIdentical(a.right, b.right)

        # following way will go one more stack (print one more 3, since \
        # still go through the right child tree "2")
        # a1 = self.isIdentical(a.left, b.left)
        # b1 = self.isIdentical(a.right, b.right)
        # return a1 and b1
