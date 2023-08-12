class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            
            m = (l + r) // 2
            
            if nums[m] == target:
                return True
            
            if nums[m] >= nums[l]:
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
        
        return False