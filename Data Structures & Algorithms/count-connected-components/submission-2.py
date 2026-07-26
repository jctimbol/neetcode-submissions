class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        print(adj_list)
        visited = set()
        components = 0

        def dfs(node):
            if node is None or node in visited:
                return
            visited.add(node)
            for neighbor in adj_list[node]:
                print(adj_list[node])
                dfs(neighbor)


        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1
        
        return components