# https: // leetcode.com/problems/binary-tree-right-side-view/
'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom

Example
Example 1

Input: {1,2,3,#,5,#,4}
Output: [1,3,4]
Explanation:
   1            
 /   \
2     3         
 \     \
  5     4       
Example 2

Input: {1,2,3}
Output: [1,3]
Explanation:
   1            
 /   \
2     3        

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs
# class Solution:
#    def rightSideView(self, root: TreeNode) -> List[int]:
#         res = []
#         if not root:
#             return res
#         self.helper(root, 0, res)
#         return res

#     def helper(self, root, level, res):
#         if not root:
#             return
#         if level == len(res):
#             res.append(root.val)
#         self.helper(root.right, level + 1, res)
#         self.helper(root.left, level + 1, res)


# bfs
class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """

    def rightSideView(self, root):
        if not root:
            return []

        # bfs
        import collections
        q = collections.deque([root])
        res = []
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
