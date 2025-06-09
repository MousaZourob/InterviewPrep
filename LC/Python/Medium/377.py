class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def dfs(curr):
            if curr in dp:
                return dp[curr]
            if curr == 0:
                return 1
            
            res = 0
            
            for num in nums:
                if curr - num >= 0:
                    res += dfs(curr - num)
            
            dp[curr] = res
            return res
            
        return dfs(target)