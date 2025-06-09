class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * (n) for _ in range(n)]
        
        
        for i in range(n-2, 0, -1):
            for j in range(i, n-1):
                for k in range(i, j + 1):
                    score = nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j]
                    dp[i][j] = max(score, dp[i][j])
                    
        return dp[1][n-2]