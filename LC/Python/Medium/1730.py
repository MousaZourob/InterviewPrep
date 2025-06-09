class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    q.append([0, [i, j]])
                    break
        
        while q:
            moves, state = q.popleft()
            r, c = state
            
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr = r + x
                nc = c + y
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] in ('#', 'O'):
                    if grid[nr][nc] == '#':
                        return moves + 1

                    q.append((moves + 1, (nr, nc)))
                    grid[nr][nc] = '-'
            
        return -1