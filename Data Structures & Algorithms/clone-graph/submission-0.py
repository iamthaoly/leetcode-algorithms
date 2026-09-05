"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        d = {}

        def clone(node):
            if node.val in d:
                return d[node.val]
            
            cp = Node(node.val)
            d[node.val] = cp

            for nb in node.neighbors:
                cp.neighbors.append(clone(nb))

            return cp

        return clone(node)