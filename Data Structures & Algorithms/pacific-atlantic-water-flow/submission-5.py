class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        res = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs_pacific(i, j, prev):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in pacific:
                return
            
            if heights[i][j] >= prev:
                pacific.add((i, j))
                for di, dj in directions:
                    dfs_pacific(i+di, j+dj, heights[i][j])
        
        def dfs_atlantic(i, j, prev):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in atlantic:
                return
            if heights[i][j] >= prev:
                atlantic.add((i, j))
                for di, dj in directions:
                    dfs_atlantic(i+di, j+dj, heights[i][j])
        
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    dfs_pacific(i, j, heights[i][j])
        
        for i in range(ROWS):
            for j in range(COLS):
                if i == ROWS - 1 or j == COLS - 1:
                    dfs_atlantic(i, j, heights[i][j])

        for (i, j) in pacific:
            if (i, j) in atlantic:
                res.append([i, j])

        return res
        
