class UnionFind:
    def __init__(self, n):
        self.Parent = list(range(n))    # each city is own parent
        self.Size = [1] * n             # sizes of each city's component
        self.components = n             # n = number of cities
    
    def find(self, node):               # goal: get root of node
        if node == self.Parent[node]:
            return node
        self.Parent[node] = self.find(self.Parent[node]) # path compression
        return self.Parent[node]

    def union(self, u, v) -> bool:             
        # check if in same component
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        # operate on roots for accurate sizing + parent assignment
        if self.Size[pu] > self.Size[pv]: # merge v into u
            self.Parent[pv] = pu
            self.Size[pu] += self.Size[pv]
        else:                               # merge u into v
            self.Parent[pu] = pv
            self.Size[pv] += self.Size[pu]
        
        self.components -= 1
        return True

    def getComponents(self):
        return self.components

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union_find = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union_find.union(i, j)
        
        return union_find.getComponents()
        