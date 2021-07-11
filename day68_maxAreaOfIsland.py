'''
Description
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

The length of each dimension in the given grid does not exceed 50.

Example
Example 1:

input:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
output : 6.
Explanation : Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

input: [[0,0,0,0,0,0,0,0]]
output : 0

'''


class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """

    def maxAreaOfIsland(self, grid):

        if not grid or not grid[0]:
            return 0

        visited = set()
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    result = max(result, self.bfs(grid, i, j, visited))
        return result

    def bfs(self, grid, x, y, visited):
        queue = collections.deque([(x, y)])
        visited.add((x, y))
        # area start from 1 not 0 because the condition is when grid[i][j] == 1 then do bfs
        area = 1
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
                    area += 1
        return area
