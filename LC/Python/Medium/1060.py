class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            mid = r - (r - l) // 2
            if (nums[mid] - nums[0]) - mid < k:
                l = mid
            else:
                r = mid - 1

        return nums[0] + k + l 