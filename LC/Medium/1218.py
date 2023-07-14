class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 0
        dp = defaultdict(int)
        
        for num in arr:
            dp[num] = dp[num - difference] + 1
            ans = max(ans, dp[num])
            
        return ans
