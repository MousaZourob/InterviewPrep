class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans, curr = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                curr = [item + [nums[i]] for item in curr]
            else:
                curr = [item + [nums[i]] for item in ans]
            ans += curr
        return ans