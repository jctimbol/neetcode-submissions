class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time = 0

        visited = set()
        q = deque()
        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    visited.add((i, j))
                    q.append((i, j))

        while q and fresh > 0:
            time += 1
            for k in range(len(q)):
                i, j = q.popleft()
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if ni < 0 or ni >= ROWS or nj < 0 or nj >= COLS:
                        continue
                    if (ni, nj) not in visited and grid[ni][nj] == 1:
                        fresh -= 1
                        grid[ni][nj] = 2
                        visited.add((ni, nj))
                        q.append((ni, nj))

        return time if not fresh else -1