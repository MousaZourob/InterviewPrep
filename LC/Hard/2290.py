class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        q = deque([(0, (0,0))])
        visited = set([(0,0)])
        
        while q:
            removed, state = q.popleft()
            r, c = state
            
            if r == m - 1 and c == n - 1:
                return removed
            
            for x, y in dirs:
                nr = r + x
                nc = c + y
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_state = (nr, nc)
                    if new_state not in visited:
                        if grid[nr][nc] == 1:
                            q.append((removed + 1, new_state))
                            visited.add(new_state)
                        else:
                            q.appendleft((removed, new_state))
                            visited.add(new_state)
        
        return -1