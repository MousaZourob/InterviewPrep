class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [(grid[0][0], 0, 0)]
        visited = [[0] * n for _ in range(n)]
        visited[0][0] = 1

        while q:
            t, r, c = heappop(q)

            if r == n - 1 and c == n - 1:
                return t

            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                n_r = r + x
                n_c = c + y

                if 0 <= n_r < n and 0 <= n_c < n and not visited[n_r][n_c]:
                    heappush(q, (max(t, grid[n_r][n_c]), n_r, n_c))
                    visited[n_r][n_c] = 1

        return -1