class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        
        window_start = 0
        ans = 0
        prod = 1
                
        for window_end in range(len(nums)):
            prod *= nums[window_end]

            while prod >= k:
                prod /= nums[window_start]
                window_start += 1
            ans += window_end - window_start + 1
                
        return ans