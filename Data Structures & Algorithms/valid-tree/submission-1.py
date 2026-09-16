class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        print(adj_list)

        #check cycle
        visited = set()
        curr = 0
        def cycle(node, parent):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    if cycle(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False
                
        if cycle(curr, None):
            print('has cycle')
            return False

        #check if all nodes reachable
        if len(visited) != n:
            print('nodes not reachable')
            return False
        
        return True