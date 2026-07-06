class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(i,j):
            q = deque([(i, j)])
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[i][j] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i,j)

                    