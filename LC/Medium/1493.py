class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window_start = 0
        zeros = 0
        ans = 0
        
        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                zeros += 1
                
            while zeros > 1:
                if nums[window_start] == 0:
                    zeros -= 1
                window_start += 1
        
            ans = max(ans, window_end - window_start)
        
        return ans