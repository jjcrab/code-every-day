# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
'''
Description
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

Example
Example 1:

Input:

tree = {1,2,3}
Output:

[[2,3],[1]]
Explanation:

    1
   / \
  2   3
it will be serialized {1,2,3}
Example 2:

Input:

tree = {3,9,20,#,#,15,7}
Output:

[[15,7],[9,20],[3]]
Explanation:

    3
   / \
  9  20
    /  \
   15   7
it will be serialized {3,9,20,#,#,15,7}

'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""




import collections
class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    def levelOrderBottom(self, root):
        # write your code here
        result = []
        if not root:
            return result

        # use deque
        queue = collections.deque()
        # put tree root to deque
        queue.append(root)
        # add each layer to result

        while queue:
            n = len(queue)
            tem = []
         # for loop,
            for i in range(n):
              # take out each element in deque
                cur = queue.popleft()
                tem.append(cur.val)
          # if left or right, append to deque
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(tem)

        return result[::-1]
