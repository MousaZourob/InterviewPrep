class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        window_start = 0

        used = 0

        for window_end in range(len(nums)):
            while used & nums[window_end] != 0:
                used ^= nums[window_start]
                window_start += 1
            used |= nums[window_end]
            ans = max(ans, window_end - window_start + 1)
        
        return ans