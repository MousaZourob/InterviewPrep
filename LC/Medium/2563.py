class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        def bin_search(nums, l, r, target):
            while l <= r:
                m = l + (r - l) // 2
                
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            
            return l
        
        ans = 0
        for i, num in enumerate(nums):
            low = bin_search(nums, i + 1, n - 1, lower - num)
            high = bin_search(nums, i + 1, n - 1, upper - num + 1)
            ans += high - low
            
        return ans