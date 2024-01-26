class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        min_num = min(nums)
        
        for num in nums:
            ans += num - min_num
        
        return ans