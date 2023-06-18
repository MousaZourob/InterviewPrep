class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = defaultdict(int)
        mod = 10 ** 9 + 7

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r,c)]
            
            res = 1
            for x, y in [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[r][c]:
                    res += dfs(x, y) % mod
            dp[(r,c)] = res
            return dp[(r,c)]

        ans = 0
        for row in range(m):
            for col in range(n):
                ans += dfs(row, col)

        return ans % mod