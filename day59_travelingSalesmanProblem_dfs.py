'''
Description
Give n cities(labeled from 1 to n), and the undirected road's cost among the cities as a three-tuple[A, B, c](i.e there is a road between city A and city B and the cost is c). We need to find the smallest cost to travel all the cities starting from 1.

1.A city can only be passed once.
2.You can assume that you can reach all the rest cities.

Example
Example 1

Input:
n = 3
tuple = [[1, 2, 1], [2, 3, 2], [1, 3, 3]]
Output: 3
Explanation: The shortest path is 1 -> 2 -> 3
Example 2

Input:
n = 1
tuple = []
Output: 0
'''


class Result:
    def __init__(self):
        self.min_cost = float('inf')


class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def minCost(self, n, roads):
        if not roads:
            return 0
        graph = self.make_graph(n, roads)
        result = Result()
        self.dfs(n, 1, roads, result, 0, set([1]), graph)
        return result.min_cost

    def dfs(self, n, current_city, roads, result, cost, visited, graph):
        # end case
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return

        for next_city in graph[current_city]:
            if next_city in visited:
                continue
            visited.add(next_city)
            self.dfs(n, next_city, roads, result, cost + graph[current_city][next_city],
                     visited, graph)
            visited.remove(next_city)

    def make_graph(self, n, roads):
        graph = {i: {} for i in range(1, n + 1)}
        for a, b, c in roads:
            if b not in graph[a]:
                graph[a][b] = c
            else:
                graph[a][b] = min(graph[a][b], c)
            if a not in graph[b]:
                graph[b][a] = c
            else:
                graph[b][a] = min(graph[b][a], c)

        return graph
