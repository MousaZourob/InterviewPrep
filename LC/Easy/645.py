class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [-1,-1]
        
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans[0] = abs(num)
            else:
                nums[abs(num) - 1] *= -1
            
        for i, num in enumerate(nums):
            if num > 0:
                ans[1] = i+1
                
        return ans