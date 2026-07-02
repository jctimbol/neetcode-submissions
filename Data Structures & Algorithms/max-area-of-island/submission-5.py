class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    island = self.mark(i, j, grid)
                    islands.append(island)
        if not islands:
            return 0
        else:
            return max(islands)

    def mark(self, i, j, grid) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
            return 0
        else:
            grid[i][j] = 0
            return 1 + self.mark(i-1, j, grid) + self.mark(i+1, j, grid)  + self.mark(i, j-1, grid) + self.mark(i, j+1, grid) 
