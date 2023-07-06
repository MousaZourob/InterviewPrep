class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = inf
        window_start = 0
        window_sum = 0
        
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            
            while window_sum >= target:
                ans = min(ans, window_end - window_start + 1)
                window_sum -= nums[window_start]
                window_start += 1
            
        return ans if ans != inf else 0