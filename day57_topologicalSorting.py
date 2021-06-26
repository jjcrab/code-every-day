'''
Description
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

You can assume that there is at least one topological order in the graph.
Learn more about representation of graphs

The number of graph nodes <= 5000
Example
Example 1:

Input:

graph = {0, 1, 2, 3  # 1,4#2,4,5#3,4,5#4#5}
         Output:

         [0, 1, 2, 3, 4, 5]
         Explanation:

         For graph as follow:

         图片

         he topological order can be:
         [0, 1, 2, 3, 4, 5]
         [0, 2, 3, 1, 5, 4]
         ...
         You only need to return any topological order for the given graph.

         Challenge
         Can you do it in both BFS and DFS?
'''


"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # get indegree for each node
        indegrees = self.get_indegree(graph)

        # put the nodes of 0 indgree into queue
        start_nodes = [n for n in graph if indegrees[n] == 0]
        queue = collections.deque(start_nodes)

        # record topo order
        topo_order = []

        # bfs take one node from queue, change indegree of neighbors
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in node.neighbors:
                indegrees[neighbor] -= 1
                # put the nodes of 0 indegree (after change) into queue
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return topo_order

    def get_indegree(self, graph):
        indegrees = {node: 0 for node in graph}
        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1
        return indegrees
