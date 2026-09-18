class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (-1, 0), (1 , 0)]
        def backtrack(position, i, j):
            if position == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[position]:
                return False

            temp, board[i][j] = board[i][j], '#'
            found = False
            for di, dj in directions:
                if backtrack(position+1, i+di, j+dj):
                    found = True
            board[i][j] = temp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(0, i, j):
                    return True
       
        return False
        