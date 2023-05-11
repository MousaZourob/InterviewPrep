class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)] 
        
        i, j = 0, -1
        dirr = 1
        
        num = 1
        while 0 < n*n:
            for _ in range(n):
                j += dirr
                ans[i][j] = num
                num += 1
            for _ in range(n - 1):
                i += dirr
                ans [i][j] = num
                num += 1
            n -= 1
            dirr *= -1
            
        return ans