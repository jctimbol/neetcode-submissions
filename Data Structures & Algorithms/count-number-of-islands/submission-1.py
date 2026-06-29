class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    self.mark(grid, i, j)
        return islands

    def mark(self, grid, i, j) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return
        if grid[i][j] == '1':
            grid[i][j] = '0'
            self.mark(grid, i-1, j)
            self.mark(grid, i, j-1)
            self.mark(grid, i+1, j)
            self.mark(grid, i, j+1)