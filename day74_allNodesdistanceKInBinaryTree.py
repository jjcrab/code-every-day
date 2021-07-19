
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
'''
We are given a binary tree (with root node root), a target node, and an integer value k.

Return a list of the values of all nodes that have a distance k from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        if not root or not target:
            return res
        # use dfs build a graph
        graph = collections.defaultdict(set)
        self.dfs(graph, root)
        # use bfs find the distance
        self.bfs(graph, target, k, res)
        return res

    def dfs(self, graph, root):
        if not root:
            return
        if root.left:
            graph[root].add(root.left)
            graph[root.left].add(root)
            self.dfs(graph, root.left)
        if root.right:
            graph[root].add(root.right)
            graph[root.right].add(root)
            self.dfs(graph, root.right)

    def bfs(self, graph, target, k, res):

        q = collections.deque([target])
        dist = 0
        visited = set([target])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if dist == k:
                    res.append(node.val)
                    continue

                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    q.append(neighbor)
                    visited.add(neighbor)
            dist += 1
