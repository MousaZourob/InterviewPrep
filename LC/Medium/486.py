class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        
        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            if l == r:
                return nums[l]
            
            left = nums[l] - dfs(l + 1, r)
            right = nums[r] - dfs(l, r - 1)
            
            dp[(l,r)] = max(left, right)
            
            return max(left, right)
        
        return dfs(0, len(nums) - 1) >= 0