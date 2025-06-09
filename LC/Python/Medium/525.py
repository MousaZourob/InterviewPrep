class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        indexes = {-1: 0}
        ans = 0 
        count = 0
        
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            
            if count in indexes:
                ans = max(ans, i - indexes[count])
            else:
                indexes[count] = i
        
        return ans