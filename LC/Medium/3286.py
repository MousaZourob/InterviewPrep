class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0]: health -= 1
        q = deque([(health, [0, 0])])

        while q:
            health, state = q.popleft()
            r, c = state
            
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr = r + x
                nc = c + y
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != '-':
                    if health - grid[nr][nc] < 1:
                        continue
                    if nr == m - 1 and nc == n - 1:
                        return True
                    
                    if grid[nr][nc]:
                        q.append((health - 1, (nr, nc)))
                        grid[nr][nc] = '-'
                    else:
                        q.appendleft((health, (nr, nc)))
                        grid[nr][nc] = '-'
            
        return False