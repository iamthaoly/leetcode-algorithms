"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Practice
        # pattern: connected graph, clone graph, adj list
        # mistakes:
        # - not handle empty graph
        
        def dfs(cur):
            # if not cur.neighbors:
            #     return Node(cur.val + 1)
            
            # visited.add(cur.val)
            # res = []
            if cur.val in graph:
                return graph[cur.val]

            graph[cur.val] = Node(cur.val)
            res = []
            for nb in cur.neighbors:
                res.append(dfs(nb))

            graph[cur.val].neighbors = res
            return graph[cur.val]
        if not node:
            return node

        graph = {}
        return dfs(node)