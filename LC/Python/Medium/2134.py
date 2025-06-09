class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        window_size = sum(nums)
        window_start = 0
        
        count = 0
        for window_end in range(len(nums)*2):
            if nums[window_end % n] == 1:
                count += 1
            
            while window_end - window_start + 1 > window_size:
                count -= nums[window_start % n]
                window_start += 1
            
            ans = min(ans, window_size - count)
        
        return ans