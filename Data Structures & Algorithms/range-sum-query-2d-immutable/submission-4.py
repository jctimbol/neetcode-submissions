class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []

        for row in matrix:
            prefix_row = [row[0]]
            for col in row[1:]:
                prefix_row.append(col + prefix_row[-1])
            self.prefix.append(prefix_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_sum = 0
        for i in range(row1, row2+1):
            if col1-1 < 0:
                total_sum += self.prefix[i][col2]
            else:
                total_sum += (self.prefix[i][col2] - self.prefix[i][col1-1])
        return total_sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)