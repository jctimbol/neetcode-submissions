class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    island = self.mark(i, j, grid, 1)
                    islands.append(island)
        if not islands:
            return 0
        else:
            return max(islands)

    def mark(self, i, j, grid, count) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
            return 0
        else:
            grid[i][j] = 0
            return 1 + self.mark(i-1, j, grid, count) + self.mark(i+1, j, grid, count)  + self.mark(i, j-1, grid, count) + self.mark(i, j+1, grid, count) 
'''
0,0,1,0,0,0,0,1,0,0,0,0,0
0,0,0,0,0,0,0,1,1,1,0,0,0
0,1,1,0,1,0,0,0,0,0,0,0,0
0,1,0,0,1,1,0,0,1,0,1,0,0
0,1,0,0,1,1,0,0,1,1,1,0,0
0,0,0,0,0,0,0,0,0,0,1,0,0
0,0,0,0,0,0,0,1,1,1,0,0,0
0,0,0,0,0,0,0,1,1,0,0,0,0
[1, 4, 3, 5, 5, 5]
[1, 4, 4, 5, 6, 5]
'''