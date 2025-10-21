class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        count = Counter(nums)
        ans = 0

        for num in range(nums[0], nums[-1] + 1):
            left = bisect_left(nums, num-k)
            right = bisect_right(nums, num+k)
            ans = max(ans, min(right - left, count[num] + numOperations))

        return ans