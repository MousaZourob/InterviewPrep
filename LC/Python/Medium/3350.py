class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 0
        curr = 1

        ans = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                ans = max(ans, min(prev, curr))
                ans = max(ans, curr // 2)
                prev = curr
                curr = 1

        ans = max(ans, curr // 2)
        ans = max(ans, min(prev, curr))

        return ans
