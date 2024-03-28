class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        window_start = 0
        freq = defaultdict(int)        
        
        for window_end in range(len(nums)):
            freq[nums[window_end]] += 1

            while freq[nums[window_end]] > k:
                freq[nums[window_start]] -= 1
                window_start += 1
            
            ans = max(ans, window_end - window_start + 1)
        
        return ans