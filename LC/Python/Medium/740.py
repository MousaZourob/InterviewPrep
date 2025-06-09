class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums.sort()
        
        nums = set(nums)
        nums = list(nums)
        
        dp = {}
        
        def dfs(i):
            if i >= len(nums):
                return 0

            if i in dp:
                return dp[i]
            
            if i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                dp[i] = max(count[nums[i]] * nums[i] + dfs(i+2), dfs(i+1))
            else:
                dp[i] = count[nums[i]] * nums[i] + dfs(i+1)
                
            return dp[i]
        
        return dfs(0)