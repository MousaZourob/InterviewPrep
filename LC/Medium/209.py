class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        ans = inf
        l = 0
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            
            while curr_sum >= target:
                ans = min(ans, r-l+1)
                curr_sum -= nums[l]
                l += 1
            
        
        return ans if ans != inf else 0