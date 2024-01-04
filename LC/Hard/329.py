class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        _dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        cache = {}
        
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n):
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            res = 0
            for x, y in _dir:
                n_r = r + y
                n_c = c + x
                if 0 <= n_r < m and 0 <= n_c < n and matrix[r][c] < matrix[n_r][n_c]:
                    res = max(res, 1 + dfs(n_r, n_c))
            
            cache[(r, c)] = res
            return res
        
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, 1+dfs(i, j))
                
        return ans