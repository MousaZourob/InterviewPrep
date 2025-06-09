class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        rows = []
        cols = []
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)
        
        rows.sort()
        cols.sort()
        
        rows_med = rows[len(rows)//2]
        cols_med = cols[len(cols)//2]
        
        return sum(abs(row - rows_med) for row in rows) + sum(abs(col - cols_med) for col in cols)