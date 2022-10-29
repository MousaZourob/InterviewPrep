class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        window_start = 0
        
        zero_count = 0
        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                zero_count += 1
            
            while zero_count > 1 and window_start < window_end:
                if nums[window_start] == 0:
                    zero_count -= 1
                window_start += 1
                
            ans = max(ans, window_end - window_start + 1)
        
        
        return ans