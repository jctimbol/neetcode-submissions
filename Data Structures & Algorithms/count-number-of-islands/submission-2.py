class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1,0), (-1,0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def mark(grid, i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return

            if grid[i][j] == '1':
                grid[i][j] = '0'
            else:
                return

            for di, dj in directions:
                mark(grid, i+di, j+dj)


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    islands += 1
                    mark(grid, i, j)

        return islands