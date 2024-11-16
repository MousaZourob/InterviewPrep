class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        n = len(nums)
        ans = [-1] * (n - k + 1)
        window_start = 0        
        
        for window_end in range(1, n):
            if nums[window_end] != nums[window_end - 1] + 1:
                window_start = window_end

            if window_end - window_start + 1 >= k:
                ans[window_end - k + 1] = nums[window_end]
        
        return ans