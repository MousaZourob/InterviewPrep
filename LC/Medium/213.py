class Solution:
    def rob(self, nums: List[int]) -> int:
        if 1 == len(nums):
            return nums[0]
        
        def rob(nums):
            memo = {}        

            def dfs(i):
                if i >= len(nums):
                    return 0

                if i in memo:
                    return memo[i]

                memo[i] = max(dfs(i + 1), dfs(i + 2) + nums[i])
                return memo[i]
        
            return dfs(0)
        
        return max(rob(nums[:-1]), rob(nums[1:]))