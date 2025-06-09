class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        ans = [-1, -1]
        
        if not nums or target not in nums:
            return ans
        
        while l < r:
            mid = (r+l)//2
            
            if nums[mid] < target:
                l = mid + 1
            else: 
                r = mid
        
        ans[0] = l
        
        while l < len(nums) and nums[l] == target:
            ans[1] = l
            l += 1
        
        return ans