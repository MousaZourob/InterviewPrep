class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        l = 0
        r = len(nums) - 1
        
        while l < r:
            if nums[r] + nums[l] < target:
                ans += r - l
                l += 1
            else:
                r -= 1
        
        return ans