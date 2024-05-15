class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(r, c):
            res = 0
            grid[r][c] += 100

            for y, x in dirs:
                n_r = r + y
                n_c = c + x
                
                if 0 <= n_r < m and 0 <= n_c < n and 0 < grid[n_r][n_c] < 101:
                    res = max(res, dfs(n_r, n_c))
            grid[r][c] -= 100

            return res + grid[r][c]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))
        
        return ans