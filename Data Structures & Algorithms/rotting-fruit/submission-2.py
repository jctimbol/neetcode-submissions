class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        fresh = 0
        time = 0

        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i, j])
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    elif grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append([nr, nc]) 

            time += 1
                

        return -1 if fresh != 0 else time
