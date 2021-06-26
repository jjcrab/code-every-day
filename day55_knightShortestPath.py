'''
Description
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.

source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Example
Example 1:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
Example 2:

Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output:-1

'''


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortestPath(self, grid, source, destination):
        if not grid:
            return -1

        # bfs
        queue = collections.deque([(source.x, source.y)])
        visited = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return visited[(x, y)]
            for i, j in [(x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2),
                         (x - 1, y - 2), (x + 2, y +
                                          1), (x + 2, y - 1), (x - 2, y + 1),
                         (x - 2, y - 1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 0 and (i, j) not in visited:
                    queue.append((i, j))
                    visited[(i, j)] = visited[(x, y)] + 1

        return -1
