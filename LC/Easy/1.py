class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        
        for i in range(len(nums)):
            if target - nums[i] in diff:
                return [diff[target - nums[i]], i]
                
            diff[nums[i]] = i
        
        return [-1,-1]