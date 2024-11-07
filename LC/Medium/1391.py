class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dirs = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(1, 0), (0, -1)],
            4: [(0, 1), (1, 0)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)]
        }
        visited = set()    
        m = len(grid)
        n = len(grid[0])
        
        def dfs(r, c):
            visited.add((r, c))
            if (r, c) == (m-1, n-1):
                return True
            
            for x,y in dirs[grid[r][c]]:
                n_r = x + r
                n_c = y + c
                if 0<= n_r < m and 0<= n_c < n and (n_r, n_c) not in visited and (-x, -y) in dirs[grid[n_r][n_c]]:
                    if dfs(n_r, n_c):
                        return True
            return False
        
        return dfs(0, 0)