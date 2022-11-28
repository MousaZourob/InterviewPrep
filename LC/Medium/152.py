class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = nums[0]
        min_num = nums[0]
        ans = nums[0]
        
        for num in nums[1:]:
            max_num, min_num = max(max_num * num, num, min_num * num), min(max_num * num, num, min_num * num)
            
            ans = max(ans, max_num)
            
        
        return ans