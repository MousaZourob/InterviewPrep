class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        i, j = 0, -1
        dirr = 1
        
        ans = []
        
        while 0 < m*n:
            for _ in range(n):
                j += dirr
                ans.append(matrix[i][j])
            m -= 1
            for _ in range(m):
                i += dirr
                ans.append(matrix[i][j])
            n -= 1
            dirr *= -1
            
        return ans