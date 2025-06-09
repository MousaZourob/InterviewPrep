class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        
        q = [(0, (0, 0))]
        visited = set()
        
        while q:
            time, state = heappop(q)
            r, c = state
            
            if r == m - 1 and c == n - 1:
                return time
            
            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            for x, y in dirs:
                nr = r + x
                nc = c + y
                
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    wait_time = (1 if (grid[nr][nc] - time) % 2 == 0 else 0)
                    next_time = max(grid[nr][nc] + wait_time, time + 1)
                    heapq.heappush(q, (next_time, (nr, nc)))
        
        return -1