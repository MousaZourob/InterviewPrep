class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        expanded_grid = [[0] * (n * 3) for _ in range(n * 3)]
        
        for r in range(n):
            for c in range(n):
                i = r * 3
                j = c * 3
                if grid[r][c] == '\\':
                    expanded_grid[i][j] = 1
                    expanded_grid[i+1][j+1] = 1
                    expanded_grid[i+2][j+2] = 1
                elif grid[r][c] == '/':
                    expanded_grid[i][j+2] = 1
                    expanded_grid[i+1][j+1] = 1
                    expanded_grid[i+2][j] = 1
        
        def dfs(i, j):
            expanded_grid[i][j] = 1
            for x, y in dirs:
                n_x = i + x
                n_y = j + y
                
                if 0 <= n_x < n * 3 and 0 <= n_y < n * 3 and expanded_grid[n_x][n_y] == 0:
                    dfs(n_x, n_y)
        
        ans = 0
        for r in range(n * 3):
            for c in range(n * 3):
                if expanded_grid[r][c] == 0:
                    dfs(r, c)
                    ans += 1
        
        return ans