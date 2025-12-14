class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9+7
        n = len(corridor)
        dp = [[-1] * 3 for _ in range(n + 1)]
        dp[-1][0] = 0
        dp[-1][1] = 0
        dp[-1][2] = 1

        for i in range(n - 1, -1, -1):
            if corridor[i] == 'S':
                dp[i][0] = dp[i + 1][1]
                dp[i][1] = dp[i + 1][2]
                dp[i][2] = dp[i + 1][1]
            else:
                dp[i][0] = dp[i + 1][0]
                dp[i][1] = dp[i + 1][1]
                dp[i][2] = (dp[i + 1][0] + dp[i + 1][2]) % mod
        
        return dp[0][0]
