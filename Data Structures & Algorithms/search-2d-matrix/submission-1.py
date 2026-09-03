class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        row = 0

        while (l <= r):
            mid = (l + r) // 2
            if matrix[mid][0] < target: # see if next rows are still less
                row = mid
                l = mid + 1
            elif matrix[mid][0] == target:
                return True
            else:
                r = mid - 1
        
        l = 0
        r = len(matrix[row]) - 1
    
        while (l <= r):
            mid = (l + r) // 2
            if matrix[row][mid] < target: 
                l = mid + 1
            elif matrix[row][mid] == target:
                return True
            else:
                r = mid - 1
        
        return False
