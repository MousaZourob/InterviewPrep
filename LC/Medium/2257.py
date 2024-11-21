class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0], [0,-1], [-1, 0]]
        grid = [[0] * n for _ in range(m)]
        ans = m * n
        for r, c in walls + guards:
            grid[r][c] = 2
            ans -= 1
    
        for r, c in guards:
            for x, y in dirs:
                nr = r + x
                nc = c + y
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2:
                    if grid[nr][nc] == 0:
                        ans -= 1
                    grid[nr][nc] = 1
                    nr += x
                    nc += y 
            
        return ans