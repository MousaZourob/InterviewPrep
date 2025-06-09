class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        max_e = max(nums)
        max_c = 0
        window_start = 0
        
        for window_end in range(len(nums)):
            max_c += 1 if nums[window_end] == max_e else 0
            
            while max_c >= k:
                max_c -= 1 if nums[window_start] == max_e else 0
                window_start += 1
            
            ans += window_start
        
        return ans
