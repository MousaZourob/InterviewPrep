class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == n:
                return True
            
            ans = False
            if i < len(nums) - 1 and nums[i] == nums[i+1]:
                ans = dfs(i+2)
            if i < len(nums) - 2:
                if (nums[i] == nums[i+1] == nums[i+2]) or (nums[i] == nums[i+1] - 1 == nums[i+2]-2):
                    ans |= dfs(i+3)
                    
            dp[i] = ans
            return ans
        
        return dfs(0)