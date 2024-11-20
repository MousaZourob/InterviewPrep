class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window_start = 0
        seen = set()
        curr_sum = 0
        ans = 0
        
        for window_end, num  in enumerate(nums):
            while num in seen:
                seen.remove(nums[window_start])
                curr_sum -= nums[window_start]
                window_start += 1
            
            curr_sum += num
            seen.add(num)
    
            if window_end - window_start + 1 >= k:
                ans = max(ans, curr_sum)
                seen.remove(nums[window_start])
                curr_sum -= nums[window_start]
                window_start += 1
            
        return ans