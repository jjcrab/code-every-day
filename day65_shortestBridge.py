'''
Description
In a given 2D binary array A, there are two islands. (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped. (It is guaranteed that the answer is at least 1.)

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
Example
Example 1:

Input：[[0,1],[1,0]]
Output：1
Explanation：Flip 0 on (0,0) or (1,1)
Example 2:

Input：[[0,1,0],[0,0,0],[0,0,1]]
Output：2
Explanation：Flip 0 on (0,2) and (1,2)
'''


class Solution:
    def ShortestBridge(self, A):
        # find fist island point
        flag = False
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    start = (i, j)
                    flag = True
                    break
            if flag:
                break

        print(start)

        # bfs find the fist island all points
        queue_firstisland = collections.deque([start])
        first_island_points = set([start])
        while queue_firstisland:
            x, y = queue_firstisland.popleft()
            for i, j in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:

                if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
                    continue
                if (i, j) in first_island_points:
                    continue
                if A[i][j] != 1:
                    continue
                queue_firstisland.append((i, j))
                first_island_points.add((i, j))

        first_island_list = list(first_island_points)

        # bfs find the shortest steps from 1st island (each 1st island points) to 2nd island
        step = 0
        queue = collections.deque(first_island_list)
        visited = set(first_island_list)
        # visited = {}
        # for i in first_island_list:
        #     visited[i] = 0
        # print(visited)
        while queue:
            # by layer / by level
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                # 1st island point of 2nd island
                if step > 0 and A[x][y] == 1:
                    return step - 1
                for i, j in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                    if self.isvalid(i, j, A, visited):
                        queue.append((i, j))
                        visited.add((i, j))

            step += 1

        # return step

    def isvalid(self, x, y, A, visited):
        if (x, y) in visited:
            return False
        if x < 0 or x >= len(A) or y < 0 or y >= len(A[0]):
            return False
        return True
