class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.components = n
    
    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        parent_u, parent_v = self.find(u), self.find(v)
        if parent_u == parent_v:
            return
        
        if self.size[parent_u] > self.size[parent_v]:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        else:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]

        self.components -= 1

    def getComponents(self):
        return self.components

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UF(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        
        return uf.getComponents()