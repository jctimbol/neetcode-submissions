class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def backtrack(position, i, j):
            if position == len(word):
                return True
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] != word[position]:
                return False

            temp, board[i][j] = board[i][j], '#'
            found = False

            for di, dj in directions:
                if backtrack(position+1, i+di, j+dj):
                    found = True

            board[i][j] = temp
            return found

        
        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(0, i, j):
                    return True
        
        return False