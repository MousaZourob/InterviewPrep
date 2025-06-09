class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def find_max(x, y):
            res = 0
            for i in range(x, x+3):
                for j in range(y, y+3):
                    res = max(res, grid[i][j])
            
            return res
        
        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n -2 )]
        for i in range(n - 2):
            for j in range(n - 2):
                ans[i][j] = find_max(i, j)
        
        return ans