class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        
        min_found = -1
        max_found = -1
        window_start = 0

        for window_end in range(len(nums)):
            if nums[window_end] < minK or nums[window_end] > maxK:
                min_found = -1
                max_found = -1
                window_start = window_end + 1
                
            if nums[window_end] == minK:
                min_found = window_end
            if nums[window_end] == maxK:
                max_found = window_end

            ans += max(0, min(min_found, max_found) - window_start + 1)
            
        return ans