class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        while q and fresh > 0:
            print(q, grid)
            rotten = len(q)
            for k in range(rotten):
                i, j = q.popleft()
                for di, dj in dirs:
                    ni, nj = i+di, j+dj
                    if ni < 0 or ni >= ROWS or nj < 0 or nj >= COLS or grid[ni][nj] == 0:
                        continue
                    if grid[ni][nj] == 1:
                        fresh -= 1
                        grid[ni][nj] = 2
                        q.append((ni, nj))
            time += 1

        return time if not fresh else -1
'''
2 2 0
0 2 2
0 2 2'''