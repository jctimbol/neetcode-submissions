class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, from_edge):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in visited or board[i][j] == 'X':
                return
            visited.add((i, j))
            if board[i][j] == 'O':
                board[i][j] = 'T'
                for di, dj in directions:
                    dfs(i+di, j+dj, from_edge)
        

        for i in range(ROWS):
            dfs(i, 0, True)
            dfs(i, COLS - 1, True)
        
        for j in range(COLS):
            dfs(0, j, True)
            dfs(ROWS - 1, j, True)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                        