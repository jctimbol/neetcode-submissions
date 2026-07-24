class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        visited = set()

        for u, v in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)
        
        print(adj_list)

        components = 0

        def dfs(node):
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

            

        for i in adj_list:
            if i not in visited:
                components += 1
                dfs(i)
        
        return components