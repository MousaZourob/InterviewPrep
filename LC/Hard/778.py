class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[0] * n for _ in range(n)]
        visited[0][0] = 1
                
        q = [(grid[0][0], 0, 0)]
        
        while q:
            elevation, r, c = heappop(q)
            
            if r == n - 1 and c == n - 1:
                return elevation            
            
            for x, y in dirs:
                n_r, n_c = r + x, c + y
                
                if 0 <= n_r < n and 0 <= n_c < n and not visited[n_r][n_c]:
                    heappush(q, (max(elevation, grid[n_r][n_c]), n_r, n_c))
                    visited[n_r][n_c] = 1

                
        return -1