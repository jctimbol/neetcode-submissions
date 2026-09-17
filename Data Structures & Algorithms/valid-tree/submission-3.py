class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(n)}

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        #check for cycle
        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif parent != neighbor:
                    return True
            return False
        

        if dfs(0, None):
            return False
        
        if len(visited) != n:
            return False
        
        return True
                