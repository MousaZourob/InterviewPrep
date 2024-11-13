class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        
        for i, num in enumerate(nums):
            low = bisect_left(nums, lower - nums[i], i + 1)
            high = bisect_right(nums, upper - nums[i], i + 1)
            
            ans += high - low
            
        return ans