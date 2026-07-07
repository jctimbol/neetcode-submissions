class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = 0
        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        
        print(q)
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 2:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                            continue
                        else:
                            grid[nr][nc] = 2
                            q.append([nr, nc])
                            fresh -= 1

            time += 1
        print(grid)
        return -1 if fresh > 0 else time