'''
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
Example 4:

Input: root = []
Output: []
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        # hashmap + bfs
        import collections
        res = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        mincol = 0
        maxcol = 0

        # bfs and record col
        while queue:
            node, col_idx = queue.popleft()
            if node:
                res[col_idx].append(node.val)
                mincol = min(mincol, col_idx)
                maxcol = max(maxcol, col_idx)
                queue.append((node.left, col_idx - 1))
                queue.append((node.right, col_idx + 1))
        # print(sorted(res))

        # return [res[i] for i in sorted(res)]
        return [res[x] for x in range(mincol, maxcol+1)]
