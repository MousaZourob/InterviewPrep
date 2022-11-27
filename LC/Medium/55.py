class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= max_pos:
                max_pos = i
        
        return True if max_pos == 0 else False