class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr_low = inf
        ans = 0
        
        for num in nums:
            curr_low = min(curr_low, num)
            ans = max(ans, num - curr_low)
      
        return ans if ans != 0 else -1