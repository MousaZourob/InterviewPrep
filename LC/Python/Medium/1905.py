class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:  
        m = len(grid1)
        n = len(grid1[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n and grid2[r][c] == 1):
                return True
            
            if grid1[r][c] == 0:
                return False
            
            grid2[r][c] = 0
            
            res = True
            for x, y in dirs:
                n_r = r + x
                n_c = c + y
                res = dfs(n_r, n_c) & res
            
            return res
            
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] and grid1[i][j] and dfs(i, j):
                    ans += 1
        
        return ans