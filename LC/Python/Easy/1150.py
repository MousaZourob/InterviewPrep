class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l = bisect_left(nums, target)
        half = len(nums) // 2
        return l + half < len(nums) and nums[l + half] == target