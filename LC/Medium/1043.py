class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        dp[0] = arr[0]
        
        
        for i in range(n-1, -1, -1):
            curr_max = 0
    
            for j in range(i, min(i+k, n)):
                curr_max = max(curr_max, arr[j])
                dp[i] = max(dp[i], curr_max * (j - i + 1) + dp[j+1])
        
        return dp[0]