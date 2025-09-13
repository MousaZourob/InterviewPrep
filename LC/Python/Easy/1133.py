class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        return max((k for k, v in count.items() if v == 1), default=-1)