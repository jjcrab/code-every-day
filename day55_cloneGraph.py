'''
Description
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

You need return the node with the same label as the input node.
How we represent an undirected graph: http://www.lintcode.com/help/graph/

Example
Example1

Input:
{1,2,4#2,1,4#4,1,2}
Output: 
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2  
 \     |  
  \    |  
   \   |  
    \  |  
      4   
'''

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # find all the vertexes
        # bfs
        root = node
        if not node:
            return node

        nodes = self.getnodes(node)

        # copy all the vertexes
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        # copy all the edges
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getnodes(self, node):
        q = collections.deque([node])
        visited = set([node])
        while q:
            curt_node = q.popleft()
            for neighbor in curt_node.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return visited

# testing: {1,2,4#2,1,4#4,1,2}


# method 2
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # bfs
        if not node:
            return node
        q = collections.deque([node])
        visited = {node: UndirectedGraphNode(node.label)}

        while q:
            curt_node = q.popleft()
            for neig in curt_node.neighbors:
                if neig not in visited:
                    q.append(neig)
                    visited[neig] = UndirectedGraphNode(neig.label)
                visited[curt_node].neighbors.append(visited[neig])

        return visited[node]


# https://leetcode.com/problems/clone-graph/
'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
Example 4:


Input: adjList = [[2],[1]]
Output: [[2],[1]]
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        q = collections.deque([node])
        visited = {node: Node(node.val, [])}
        while q:
            curt_node = q.popleft()
            for neig in curt_node.neighbors:
                if neig not in visited:
                    q.append(neig)
                    visited[neig] = Node(neig.val, [])
                visited[curt_node].neighbors.append(visited[neig])

        return visited[node]
