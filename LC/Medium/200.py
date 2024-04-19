class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        _dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        
        def dfs(x, y):
            grid[x][y] = '0'
            for r_x, r_y in _dir:
                n_r, n_c = r_x + x, r_y + y
                if 0 <= n_r < m and 0 <= n_c < n and grid[n_r][n_c] == '1':
                    dfs(n_r, n_c)
            
        ans = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r,c)
                    ans += 1
        return ans