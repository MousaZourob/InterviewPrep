class Solution:
    def findDerangement(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 0
        
        dp = [0]*(n + 1)
        dp[0] = 1
        dp[1] = 0
        
        for i in range(2, n + 1):
            dp[i] = (i - 1)*(dp[i - 1] + dp[i - 2]) % 1000000007

        return dp[n]