class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0 for _ in range(26)]
        ans = 1
        
        for ch in s:
            i = ord(ch) - ord('a')
            dp[i] = dp[i] + 1
            
            for j in range(max(0, i - k), min(25, i + k) + 1):
                if j != i:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            ans = max(ans, dp[i])
        
        return ans