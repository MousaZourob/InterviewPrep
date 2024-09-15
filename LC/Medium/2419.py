class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        max_val = 0
        curr = 0
        for num in nums:
            if num > max_val:
                max_val = max(max_val, num)
                ans = 1
                curr = 1
            elif max_val == num:
                curr += 1
            else:
                curr = 0
            ans = max(ans, curr)
            
        return ans