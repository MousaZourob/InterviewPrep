class Solution:
    def rob(self, nums: List[int]) -> int:
        if 1 == len(nums):
            return nums[0]
        
        def rob(nums: List[int]) -> int:
            rob = not_rob = 0

            for n in nums:
                rob, not_rob = max(not_rob + n, rob), rob

            return rob
        
        return max(rob(nums[:-1]), rob(nums[1:]))