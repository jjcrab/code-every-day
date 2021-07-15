# https: // leetcode.com/problems/number-of-provinces/submissions/
'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
'''


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # use bfs
        # edge case
        n = len(isConnected)
        if n < 2:
            return n

        # create a graph
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)

        # bfs
        res = 0
        visited = set()

        for c in range(n):
            if c in visited:
                continue
            queue = collections.deque([c])
            visited.add(c)

            while queue:
                city = queue.popleft()
                neighbours = graph[city]
                for neighbour in neighbours:
                    if neighbour in visited:
                        continue
                    queue.append(neighbour)
                    visited.add(neighbour)
            res += 1
        return res
