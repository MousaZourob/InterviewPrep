class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.prefix = [[0] * self.n for _ in range(self.m)]
        
        for r in range(self.m):
            curr_sum = 0
            for c in range(self.n):
                curr_sum += matrix[r][c]
                self.prefix[r][c] = curr_sum
                if r != 0:
                    self.prefix[r][c] += self.prefix[r-1][c]        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int  ) -> int:
        ans = self.prefix[row2][col2] 
        if col1 != 0:
            ans -= self.prefix[row2][col1-1]
        if row1 != 0:
            ans -= self.prefix[row1-1][col2]
        if row1 != 0 and col1 != 0:
            ans += self.prefix[row1-1][col1-1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)