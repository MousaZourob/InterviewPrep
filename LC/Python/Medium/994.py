class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = []
        ans = 0
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.pop(0)
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + x
                    nc = c + y

                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            ans += 1
        
        return ans if fresh == 0 else -1
            
