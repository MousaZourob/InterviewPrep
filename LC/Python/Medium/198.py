class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = not_rob = 0
        
        for n in nums:
            rob, not_rob = max(not_rob + n, rob), rob

        return rob