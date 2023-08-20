class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(grid)
        n = len(grid[0])
        q = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q:
            r, c = q.pop(0)
            
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + x
                nc = c + y
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append([nr, nc])
        
        