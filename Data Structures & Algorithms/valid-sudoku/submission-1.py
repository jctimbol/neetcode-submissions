class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force
        
        visited = set()
        #check rows
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in visited:
                        print('row', board[i][j], visited)
                        return False
                    else:
                        visited.add(board[i][j])
            visited = set()

        visited = set()
        #check cols
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[j][i] != '.':
                    if board[j][i] in visited:
                        print('col', j, i, visited)
                        return False
                    else:
                        visited.add(board[j][i])

            visited = set()
        
        visited = set()
        #check squares
        for i in range(0,len(board), 3):
            for j in range(0, len(board[0]), 3):
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != '.':
                            if board[k][l] in visited:
                                print('square')
                                return False
                            else:
                                visited.add(board[k][l])
                visited = set()

        

        return True

'''
[[".",".","4",".",".",".","6","3","."],
 [".",".",".",".",".",".",".",".","."],
 ["5",".",".",".",".",".",".","9","."],
 [".",".",".","5","6",".",".",".","."],
 ["4",".","3",".",".",".",".",".","1"],
 [".",".",".","7",".",".",".",".","."],
 [".",".",".","5",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."]]

'''