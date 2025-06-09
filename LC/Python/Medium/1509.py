class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        ans = inf
        nums.sort()

        for i in range(4):
            ans = min(ans, nums[n - 4 + i] - nums[i])
        return ans