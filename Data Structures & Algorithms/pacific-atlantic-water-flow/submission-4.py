class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        cells = []
        
        def dfs(i, j, height, visited):
            #we're doing it in reverse, so height cond is reversed
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or heights[i][j] < height or (i, j) in visited:
                return

            curr_height = heights[i][j]
            visited.add((i, j))
            dfs(i+1, j, curr_height, visited)
            dfs(i, j+1, curr_height, visited)
            dfs(i-1, j, curr_height, visited)
            dfs(i, j-1, curr_height, visited)
        
        for i in range(ROWS):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, COLS-1, heights[i][COLS-1], atl)
        
        for j in range(COLS):
            dfs(0, j, heights[0][j], pac)
            dfs(ROWS-1, j, heights[ROWS-1][j], atl)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pac and (i, j) in atl:
                    cells.append([i, j])
        
        return cells