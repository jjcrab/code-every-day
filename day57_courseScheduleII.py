'''
Description
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0, 1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example
Example 1:

Input: n = 2, prerequisites = [[1, 0]]
Output: [0, 1]
Example 2:

Input: n = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: [0, 1, 2, 3] or [0, 2, 1, 3]
'''


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """

    def findOrder(self, numCourses, prerequisites):
        # create a graph, index(class) -- neighbors
        graph = [[] for i in range(numCourses)]
        # get indegree for each class, index(class) -- indegree
        in_degree = [0] * numCourses
        # fill/complete the graph and indegrees
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] += 1

        # put the indegree == 0 class into queue as start class
        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        topo_order = []
        # bfs, pop the first class in queue and change the indegree for the neighbors
        while queue:
            cur_class = queue.popleft()
            topo_order.append(cur_class)
            for neighbor in graph[cur_class]:
                in_degree[neighbor] -= 1
                # put the indegree == 0 class (after change) into queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # if has self cycle node?
        if len(topo_order) != numCourses:
            return []
        return topo_order
