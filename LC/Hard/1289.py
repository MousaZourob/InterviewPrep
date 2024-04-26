class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = {}
        
        def dfs(curr_row, prev_col):
            if (curr_row, prev_col) in dp:
                return dp[(curr_row, prev_col)]
            
            if curr_row >= n:
                return 0
            
            res = inf
            for j in range(n):
                if j != prev_col:
                    res = min(res, grid[curr_row][j] + dfs(curr_row + 1, j))
               
            dp[(curr_row, prev_col)] = res
            return res  
        
        ans = inf
        for i in range(n):
            ans = min(ans, grid[0][i] + dfs(1, i))
            
        return ans