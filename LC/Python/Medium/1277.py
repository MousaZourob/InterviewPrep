class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = {}
        
        def dfs(r, c):
            if r == n or c == m or matrix[r][c] == 0:
                return 0
            
            if (r, c) in dp:
                return dp[(r,c)]
            
            dp[(r,c)] = 1 + min(
                dfs(r + 1, c),
                dfs(r, c + 1),
                dfs(r + 1, c + 1)
            )
            
            return dp[(r,c)]
        
        ans = 0
        for r in range(n):
            for c in range(m):
                ans += dfs(r, c)
                
        return ans