class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for row in range(n-2, -1, -1):
            for col in range(n):
                left = inf if col == 0 else matrix[row+1][col-1]
                down = matrix[row+1][col]
                right = inf if col == n-1 else matrix[row+1][col+1]
            
                matrix[row][col] += min(left, down, right)
                
        return min(matrix[0])