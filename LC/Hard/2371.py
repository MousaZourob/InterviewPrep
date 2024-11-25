class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        max_rows = [1] * m
        max_cols = [1] * n
        
        nums = []
        for i in range(m):
            for j in range(n):
                nums.append((grid[i][j], i, j))
                
        nums.sort()
        
        for n, i, j in nums:
            val = max(max_rows[i], max_cols[j])
            grid[i][j] = val
            max_rows[i] = val + 1
            max_cols[j] = val + 1
            
        return grid