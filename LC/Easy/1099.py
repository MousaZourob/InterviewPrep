class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return -1
        ans = -1
        nums.sort()
        i, j = 0, len(nums)-1
        
        while i < j:
            if nums[i] + nums[j] < k:
                ans = max(nums[i] + nums[j],ans)
                i += 1
            else:
                j -= 1
        
        
        return ans