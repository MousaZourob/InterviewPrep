class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        result = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            result |= num | prefix_sum

        return result