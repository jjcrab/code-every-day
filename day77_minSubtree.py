'''
escription
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
The range of input and output data is in int.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

Example
Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5 
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.

'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""




import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    # def findSubtree(self, root):
    #     # Divide Conquer + Traverse
    #     # not "-inf" , is "inf"
    #     self.minsum = float('inf')
    #     self.minsumroot = None
    #     self.findsum(root)
    #     return self.minsumroot

    # def findsum(self, root):
    #     if not root:
    #         return 0

    #     left = self.findsum(root.left)
    #     right = self.findsum(root.right)
    #     subsum = root.val + left + right

    #     if subsum < self.minsum:
    #         self.minsum = root.val + left + right
    #         self.minsumroot = root
    #     return subsum


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # Divide and Conquer
        minsumroot, minsum, sumsub = self.helper(root)
        return minsumroot

    def helper(self, root):
        if not root:
            return None, sys.maxsize, 0
        left_minsumroot, left_minsum, left_sumsub = self.helper(root.left)
        right_minsumroot, right_minsum, right_sumsub = self.helper(root.right)
        sumsub = left_sumsub + right_sumsub + root.val
        # if left tree is the min, return left tree
        if left_minsum == min(left_minsum, right_minsum, sumsub):
            return left_minsumroot, left_minsum, sumsub
        # if right tree is the min, return right tree
        if right_minsum == min(right_minsum, left_minsum, sumsub):
            return right_minsumroot, right_minsum, sumsub
        # if root is the min, return root
        return root, sumsub, sumsub
