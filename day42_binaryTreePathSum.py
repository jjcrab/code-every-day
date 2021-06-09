# https://leetcode.com/problems/path-sum-ii/

'''
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.

Example
Example 1:

Input:
{1,2,4,2,3}
5
Output: [[1, 2, 2],[1, 4]]
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
Example 2:

Input:
{1,2,4,2,3}
3
Output: []
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
Notice we need to find all paths from root node to leaf nodes.
1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5 
There is no one satisfying it.
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        path = []
        self.dfs(root, targetSum, path, result)
        return result

    def dfs(self, node, remaining, path, result):
        if not node:
            return
        remaining -= node.val
        path.append(node.val)
        # if leaves
        if not node.left and not node.right:
            if remaining == 0:
                result.append(path[:])
        # if not leaves
        self.dfs(node.left, remaining, path, result)
        self.dfs(node.right, remaining, path, result)
        path.pop()
