class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(1, len(edges)+1)}
        
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        print(adj_list)

        visited = set()
        check = set()

        for i in range(1, len(edges)+1):
            check.add(i)
        
        def dfs(node, parent):
            visited.add(node)

            # go through each in list
            for next in adj_list[node]:
                if next == parent:
                    continue
                if next in visited:
                    return True
                if dfs(next, node):
                    return True
        
            return False

        for i in range(len(edges)-1, -1, -1):
            visited = set()
            u = edges[i][0]
            v = edges[i][1]

            adj_list[u].remove(v)
            adj_list[v].remove(u)

            if not dfs(1, -1) and check == visited:
                return [u,v]
                      
            adj_list[u].append(v)
            adj_list[v].append(u)


        return []