"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_new = {}

        def dfs(old_node, parent):
            if old_node in old_new:
                if old_new[old_node] not in old_new[parent].neighbors:
                    old_new[parent].neighbors.append(old_new[old_node])
                if old_new[parent] not in old_new[old_node].neighbors:
                    old_new[old_node].neighbors.append(old_new[parent])
                return 

            new_node = Node(old_node.val)
            old_new[old_node] = new_node

            for neighbor in old_node.neighbors:
                dfs(neighbor, old_node)
            
        dfs(node, None)
        return old_new[node]