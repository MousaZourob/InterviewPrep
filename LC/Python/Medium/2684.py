class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = {}
        def dfs(r,c):
            if (r, c) in dp:
                return dp[(r,c)]
            res = 0
            for x in [-1,0,1]:
                nr = r + x
                nc = c + 1
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                    res = max(res, dfs(nr, nc) + 1)
            
            dp[(r,c)] = res
            return res
        
        ans = 0
        
        for i in range(m):
            ans = max(ans, dfs(i,0))
        
        return ans