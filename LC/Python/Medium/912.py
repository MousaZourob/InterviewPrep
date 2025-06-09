class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = {}
        
        for val in nums:
            count[val] = count.get(val, 0) + 1

        i = 0
        min_val = min(nums)
        max_val = max(nums)
        
        for val in range(min_val, max_val + 1, 1):
            while count.get(val, 0) > 0:
                nums[i] = val
                i += 1
                count[val] -= 1
                
        return nums