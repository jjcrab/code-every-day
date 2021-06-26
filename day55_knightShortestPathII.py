
'''
Description
Given a knight in a chessboard n * m(a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position(n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return - 1 if knight can not reached.

If the knight is at(x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
Example
Example 1:

Input:
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
Output:
3
Explanation:
[0, 0] -> [2, 1] -> [0, 2] -> [2, 3]
Example 2:

Input:
[[0, 1, 0], [0, 0, 1], [0, 0, 0]]
Output:
-1
'''


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        # bfs
        queue = collections.deque([(0, 0)])
        visited = {(0, 0): 0}

        while queue:
            (x, y) = queue.popleft()
            # if find it then return result
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return visited[(x, y)]

            # if not the result, then traverse all direaction and add the positions which satisfied all the conditions to the queue
            for (i, j) in [(x + 1, y + 2), (x - 1, y + 2), (x + 2, y + 1), (x - 2, y + 1)]:
                if 0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1 and grid[i][j] == 0 and (i, j) not in visited:
                    queue.append((i, j))
                    visited[(i, j)] = visited[(x, y)] + 1

        return -1
