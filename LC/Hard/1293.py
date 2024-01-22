class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        state = (0, 0, k)
        
        q = [(0, state)]
        seen = set([state])
        
        while q:
            steps, (r, c, eliminated) = q.pop(0)
            
            if r == m - 1 and c == n - 1:
                return steps
            
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                n_r, n_c = r + x, c + y
                
                if 0 <= n_r < m and 0 <= n_c < n:
                    new_state = (n_r, n_c, eliminated - grid[n_r][n_c])

                    if new_state not in seen and new_state[2] >= 0:
                        seen.add(new_state)
                        q.append((steps + 1, new_state))
        
        return -1