'''
Description
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example
Example 1:

Input:
{1}
0.000000
1
Output:
[1]
Explanation：
Binary tree {1},  denote the following structure:
 1
Example 2:

Input:
{3,1,4,#,2}
0.275000
2
Output:
[1,2]
Explanation：
Binary tree {3,1,4,#,2},  denote the following structure:
  3
 /  \
1    4
 \
  2
Challenge
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# O(N + logN)
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        # inorder traverse
        # binary search
        # two pointers
        if not root or k == 0:
            return []
        self.inorder_list = []
        self.inorder(root)
        res = self.findKth(self.inorder_list, target, k)
        return res

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.inorder_list.append(root.val)
        self.inorder(root.right)

    def findKth(self, inorder_list, target, k):
        # binary search
        start, end = 0, len(inorder_list) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if inorder_list[mid] < target:
                start = mid
            else:
                end = mid
        # two pointers
        ans = []
        while len(ans) < k:
            lower = abs(target - inorder_list[start]) if 0 <= start else None
            upper = abs(target - inorder_list[end]
                        ) if end < len(inorder_list) else None
            # start and end both in range, need to use not None, can't just if lower/upper, because the abs can be 0
            if lower is not None and upper is not None:
                if upper < lower:
                    ans.append(inorder_list[end])
                    end += 1
                else:
                    ans.append(inorder_list[start])
                    start -= 1
            # end out of range, here has to use 'is not None' instead of 'not upper' or lower, since upper/lower can be 0
            elif lower is not None:
                ans.append(inorder_list[start])
                start -= 1
            # start out of range
            elif upper is not None:
                ans.append(inorder_list[end])
                end += 1

        return ans


# O(NlogN)
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        nums = self.inorder(root)
        nums.sort(key=lambda x: abs(target - x))
        return nums[:k]

    def inorder(self, root):
        return (self.inorder(root.left) + [root.val] + self.inorder(root.right))if root else []
