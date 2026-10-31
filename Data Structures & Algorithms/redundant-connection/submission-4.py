class UnionFind:
    def __init__(self, n):
        self.Parent = list(range(n+1))
        self.Size = [1] * (n+1)
        self.components = n
    
    def find(self, node):
        if node == self.Parent[node]:
            return node
        self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v) # get actual parent!!
        if pu == pv:
            return False
        
        self.components -= 1
        if self.Size[pu] > self.Size[pv]:
            self.Parent[pv] = pu
            self.Size[pu] += self.Size[pv]
        else:
            self.Parent[pu] = pv
            self.Size[pv] += self.Size[pu]
        
        return True
    
    def getComponents(self):
        return self.components

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for u, v in edges:
            if uf.find(u) == uf.find(v):
                return [u, v]
            else:
                uf.union(u, v)
        
        return []