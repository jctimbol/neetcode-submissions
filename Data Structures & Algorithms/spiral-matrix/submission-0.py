class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        remaining = len(matrix) * len(matrix[0])
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        i, j = 0, 0
        while remaining > 0:
            # right
            while j < COLS and matrix[i][j] != 'X':
                res.append(matrix[i][j])
                matrix[i][j] = 'X'
                j += 1
                remaining -= 1
            i += 1
            j -= 1
            # down
            while i < ROWS and matrix[i][j] != 'X':
                res.append(matrix[i][j])
                matrix[i][j] = 'X'
                i += 1
                remaining -= 1
            
            i -= 1
            j -= 1
            # left
            while j >= 0 and matrix[i][j] != 'X':
                res.append(matrix[i][j])
                matrix[i][j] = 'X'
                j -= 1
                remaining -= 1
            i -= 1
            j += 1
            # up
            while i >= 0 and matrix[i][j] != 'X':
                res.append(matrix[i][j])
                matrix[i][j] = 'X'
                i -= 1
                remaining -= 1
            
            i += 1
            j += 1
        
        return res