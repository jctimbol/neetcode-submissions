class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        def dfs(i,j):
            if i<0 or i>=ROWS or j<0 or j>=COLS or board[i][j]!='O':
                return
            if board[i][j]=='O':
                board[i][j] = 'T'
            for dr, dc in directions:
                dfs(i+dr, j+dc)
        
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1:
                    dfs(i,j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        print(board)