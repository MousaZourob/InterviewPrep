class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        if total < abs(target) or abs(total - target) % 2 == 1:
            return 0
        
        dp = [0] * (total + 1)
        dp[0] = 1
        
        for num in nums:
            for j in range(total, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[(total + target)//2]