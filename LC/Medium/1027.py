class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans = 0
        dp = {}
        
        for i in range(len(nums)):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
        
        return max(dp.values())