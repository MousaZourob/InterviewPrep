class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        max_right = [0] * n
        
        curr_max = 0
        i = n - 1
        for num in reversed(nums):
            max_right[i] = max(num, curr_max)
            curr_max = max_right[i]
            i -= 1
        
        ans = 0
        window_start = 0
        for window_end in range(n):
            while nums[window_start] > max_right[window_end]:
                window_start += 1
                
            ans = max(ans, window_end - window_start)
        
        return ans
