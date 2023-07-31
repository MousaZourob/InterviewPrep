class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        dp = {}

        def opt(i: int, j: int) -> float:
            if (i, j) in dp:
                return dp[(i, j)]
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1.0
            if j <= 0:
                return 0.0

            dp[(i, j)] = (
                opt(i - 4, j)
                + opt(i - 3, j - 1)
                + opt(i - 2, j - 2)
                + opt(i - 1, j - 3)
            ) / 4.0
            return dp[(i, j)]

        for k in range(1, m + 1):
            if opt(k, k) > 1 - 1e-5:
                return 1.0
        return opt(m, m)