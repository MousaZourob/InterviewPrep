class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        non_dup = 1
        
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[non_dup] = nums[i]
                non_dup += 1
            i+=1
            
        return non_dup