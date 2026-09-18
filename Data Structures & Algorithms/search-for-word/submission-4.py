class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (-1, 0), (1 , 0)]
        paths = []
        visited = set()
        def backtrack(path, position, idx_i, idx_j):
            visited.add((idx_i, idx_j))
            if position == len(word):
                paths.append(path[:])
                return
            for di, dj in directions:
                ni, nj = idx_i + di, idx_j + dj
                if ni < 0 or ni >= len(board) or nj < 0 or nj >= len(board[0]):
                    continue
                if board[ni][nj] != word[position]:
                    continue
                if (ni, nj) in visited:
                    continue
                path.append(board[ni][nj])
                backtrack(path, position+1, ni, nj)
                visited.remove((ni, nj))
                path.pop()
            return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    backtrack([word[0]], 1, i, j)
        if paths:
            return True
        return False
        